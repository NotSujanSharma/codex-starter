#!/usr/bin/env python3
"""Validate the structure and Codex configuration of this starter repository."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "README.md",
    "AGENTS.md",
    "PLANS.md",
    "CODE_REVIEW.md",
    "SECURITY.md",
    ".codex/config.toml",
    "docs/PRODUCT.md",
    "docs/ARCHITECTURE.md",
    "docs/decisions/README.md",
    "plans/README.md",
    "plans/active/README.md",
    "plans/completed/README.md",
    "templates/FEATURE_BRIEF.md",
    "templates/EXECUTION_PLAN.md",
    "templates/TASK_CONTRACT.md",
    "templates/HANDOFF.md",
    "templates/REVIEW_REPORT.md",
    "templates/ADR.md",
}

EXPECTED_AGENTS = {
    "explorer": ("gpt-5.6-luna", "medium", "read-only"),
    "implementer": ("gpt-5.6-terra", "medium", "workspace-write"),
    "debugger": ("gpt-5.6-sol", "high", "workspace-write"),
    "verifier": ("gpt-5.6-terra", "medium", "workspace-write"),
    "reviewer": ("gpt-5.6-sol", "high", "read-only"),
    "documenter": ("gpt-5.6-luna", "low", "workspace-write"),
}

REASONING_LEVELS = {"minimal", "low", "medium", "high", "xhigh"}
SANDBOX_MODES = {"read-only", "workspace-write", "danger-full-access"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def load_toml(path: Path) -> dict:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"cannot parse {path.relative_to(ROOT)}: {error}") from error


def check_required_files(errors: list[str]) -> None:
    for relative in sorted(REQUIRED_FILES):
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"required file is empty: {relative}")


def check_project_config(errors: list[str]) -> None:
    path = ROOT / ".codex/config.toml"
    if not path.is_file():
        return

    try:
        config = load_toml(path)
    except ValueError as error:
        errors.append(str(error))
        return

    if config.get("model") != "gpt-5.6-sol":
        errors.append("project main model must be gpt-5.6-sol")
    if config.get("model_reasoning_effort") not in REASONING_LEVELS:
        errors.append("project model_reasoning_effort is missing or unsupported")
    if config.get("sandbox_mode") != "workspace-write":
        errors.append("project sandbox_mode must retain the workspace-write safe default")

    agents = config.get("agents")
    if not isinstance(agents, dict):
        errors.append("project config is missing the [agents] table")
        return

    if agents.get("enabled") is not True:
        errors.append("agents.enabled must be true")
    concurrency = agents.get("max_concurrent_threads_per_session")
    if not isinstance(concurrency, int) or not 1 <= concurrency <= 4:
        errors.append("agent concurrency must be an integer from 1 through 4")
    if agents.get("default_subagent_model") != "gpt-5.6-terra":
        errors.append("default subagent model must be gpt-5.6-terra")
    if agents.get("default_subagent_reasoning_effort") != "medium":
        errors.append("default subagent reasoning effort must be medium")

    max_bytes = config.get("project_doc_max_bytes")
    if not isinstance(max_bytes, int) or max_bytes <= 0:
        errors.append("project_doc_max_bytes must be a positive integer")
    else:
        instruction_size = (ROOT / "AGENTS.md").stat().st_size
        if instruction_size > max_bytes:
            errors.append(
                f"AGENTS.md is {instruction_size} bytes and exceeds "
                f"project_doc_max_bytes={max_bytes}"
            )


def check_agents(errors: list[str]) -> None:
    agent_dir = ROOT / ".codex/agents"
    if not agent_dir.is_dir():
        errors.append("missing custom agent directory: .codex/agents")
        return

    found: dict[str, Path] = {}
    for path in sorted(agent_dir.glob("*.toml")):
        try:
            agent = load_toml(path)
        except ValueError as error:
            errors.append(str(error))
            continue

        for field in ("name", "description", "developer_instructions"):
            value = agent.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path.relative_to(ROOT)} is missing non-empty {field}")

        name = agent.get("name")
        if not isinstance(name, str) or not name:
            continue
        if name in found:
            errors.append(
                f"duplicate agent name {name!r} in {found[name].relative_to(ROOT)} "
                f"and {path.relative_to(ROOT)}"
            )
        found[name] = path

        if path.stem != name:
            errors.append(f"agent filename {path.name} must match name={name!r}")
        if agent.get("model_reasoning_effort") not in REASONING_LEVELS:
            errors.append(f"{path.relative_to(ROOT)} has unsupported reasoning effort")
        if agent.get("sandbox_mode") not in SANDBOX_MODES:
            errors.append(f"{path.relative_to(ROOT)} has unsupported sandbox mode")

    missing = set(EXPECTED_AGENTS) - set(found)
    extra = set(found) - set(EXPECTED_AGENTS)
    for name in sorted(missing):
        errors.append(f"missing expected custom agent: {name}")
    for name in sorted(extra):
        errors.append(f"unexpected custom agent not registered in validator: {name}")

    for name, expected in EXPECTED_AGENTS.items():
        path = found.get(name)
        if path is None:
            continue
        agent = load_toml(path)
        actual = (
            agent.get("model"),
            agent.get("model_reasoning_effort"),
            agent.get("sandbox_mode"),
        )
        if actual != expected:
            errors.append(
                f"agent {name!r} routing is {actual!r}; expected {expected!r}"
            )


def markdown_files() -> list[Path]:
    ignored = {".git"}
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in ignored for part in path.relative_to(ROOT).parts)
    )


def check_markdown_links(errors: list[str]) -> None:
    for path in markdown_files():
        try:
            content = path.read_text(encoding="utf-8")
        except OSError as error:
            errors.append(f"cannot read {path.relative_to(ROOT)}: {error}")
            continue

        for raw_target in MARKDOWN_LINK.findall(content):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)} links outside the repository: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"broken relative link in {path.relative_to(ROOT)}: {raw_target}"
                )


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_project_config(errors)
    check_agents(errors)
    check_markdown_links(errors)

    if errors:
        print("Template validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Template validation passed: "
        f"{len(REQUIRED_FILES)} required files, "
        f"{len(EXPECTED_AGENTS)} custom agents, and local Markdown links checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

