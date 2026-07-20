#!/usr/bin/env python3
"""Fail-fast structural checks for the maintained proof DAG repository."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "dag" / "proof-dag.json"
MASTER = ROOT / "proof" / "conditional-proof.tex"
PARTS = ROOT / "proof" / "parts"

MODULES = (
    ("F51", "01-f51-disk-hessian"),
    ("H0", "02-h0-homogeneous-gap"),
    ("F65", "03-f65-disk-endpoint"),
    ("F129", "04-f129-source-envelope"),
    ("TR", "05-tr-physical-trace"),
    ("CT", "06-ct-cubic-tensor"),
    ("QB", "07-qb-bubble-reduction"),
    ("F144", "08-f144-midpoint-identity"),
    ("F148", "09-f148-material-matrix"),
    ("DF0A", "10-df0a-intrinsic-variance"),
    ("DF0B", "11-df0b-good-grid"),
    ("ZG", "12-zg-zero-gap"),
    ("PT", "13-pt-material-transport"),
    ("JP", "14-jp-joint-principal"),
    ("JC", "15-jc-joint-comparison"),
    ("NR", "16-nr-assembly"),
    ("F57", "17-f57-side-mass-moment"),
    ("A0", "18-a0-side-activation"),
    ("G0", "19-g0-global-assembly"),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def check_acyclic(edges: dict[str, list[str]]) -> None:
    state: dict[str, int] = {node: 0 for node in edges}

    def visit(node: str) -> None:
        require(state[node] != 1, f"dependency cycle reaches {node}")
        if state[node] == 2:
            return
        state[node] = 1
        for dependency in edges[node]:
            visit(dependency)
        state[node] = 2

    for node in edges:
        visit(node)


def source_tree_sha256() -> str:
    digest = hashlib.sha256()
    paths = [MASTER, ROOT / "proof" / "preamble.tex"]
    paths.extend(PARTS / f"{name}.tex" for _, name in MODULES)
    for path in paths:
        relative = path.relative_to(ROOT).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    nodes = manifest["nodes"]
    ids = [node["id"] for node in nodes]
    require(len(ids) == len(set(ids)), "duplicate conceptual node ID")
    id_set = set(ids)
    edges = {node["id"]: node.get("depends_on", []) for node in nodes}
    for node, dependencies in edges.items():
        missing = set(dependencies) - id_set
        require(not missing, f"{node} has missing dependencies: {sorted(missing)}")
    check_acyclic(edges)

    open_ids = [node["id"] for node in nodes if node["status"] == "open"]
    require(open_ids == ["JC_PL"], f"unexpected open frontier: {open_ids}")
    dependent = {node["id"] for node in nodes if node["status"] == "dependent"}
    require(
        dependent == {"JP_JC", "NR", "J0", "G0", "MAIN"},
        f"unexpected dependent set: {sorted(dependent)}",
    )

    assembly_ids = [module["id"] for module in manifest["assembly_modules"]]
    expected_ids = [module_id for module_id, _ in MODULES]
    require(assembly_ids == expected_ids, "manifest assembly order drift")

    expected_parts = [name for _, name in MODULES]
    actual_parts = sorted(path.stem for path in PARTS.glob("*.tex"))
    require(actual_parts == sorted(expected_parts), "proof part set drift")

    master = MASTER.read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{parts/([^}]+)\}", master)
    require(inputs == expected_parts, "master input order drift")
    require(r"\input{preamble}" in master, "master does not load shared preamble")
    require("Assume the pathwise LCA payment JC--PL" in master,
            "conditional assumption is missing from the main theorem")
    require("not an unconditional certificate" in master,
            "conditional status warning is missing")

    required_docs = (
        ROOT / "README.md",
        ROOT / "MAINTENANCE.md",
        ROOT / "docs" / "proof-audit.md",
        ROOT / "docs" / "wrong-routes.md",
    )
    for path in required_docs:
        require(path.exists(), f"missing maintenance document: {path.relative_to(ROOT)}")

    forbidden = ("*.aux", "*.fdb_latexmk", "*.log", "*.out", "*.toc")
    leftovers = [path.relative_to(ROOT) for pattern in forbidden for path in ROOT.rglob(pattern)]
    require(not leftovers, f"tracked/build-cache candidates remain: {leftovers}")

    print("proof DAG structure: PASS")
    print(f"conceptual nodes: {len(nodes)}; assembly modules: {len(MODULES)}")
    print("open frontier: JC_PL; dependent: JP_JC, NR, J0, G0, MAIN")
    print(f"proof source tree SHA256: {source_tree_sha256()}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print(f"proof DAG structure: FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
