#!/usr/bin/env python3
"""
Generate a scale-test Python repo with:
  - 10,000 source modules (src/module_N.py)
  - 2,500 test files (tests/test_module_N.py), 4 tests each = 10,000 tests total
    Each test file imports from 4 consecutive source modules:
      test_module_1  → src/module_1,  module_2,  module_3,  module_4
      test_module_2  → src/module_5,  module_6,  module_7,  module_8
      ...
      test_module_2500 → src/module_9997, module_9998, module_9999, module_10000
  - 100 fake JSON config files (configs/config_N.json)

This increases the hash array from ~606 (1k-test setup) to ~12,605 entries,
stressing the GIN index in SkipTestsIfPossible significantly.
"""

import json
import os
import random
import shutil

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR   = os.path.join(REPO_ROOT, "src")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
CONFIGS_DIR = os.path.join(REPO_ROOT, "configs")

NUM_TEST_FILES   = 2500   # 2500 test files × 4 tests = 10,000 tests
TESTS_PER_FILE   = 4
MODULES_PER_TEST = 4      # each test file imports from 4 source modules
NUM_SOURCE_FILES = NUM_TEST_FILES * MODULES_PER_TEST  # 10,000 source modules
NUM_CONFIGS      = 100

OPERATIONS = ["add", "subtract", "multiply", "divide", "modulo", "power", "min", "max"]


def clean_dirs():
    for d in [SRC_DIR, TESTS_DIR, CONFIGS_DIR]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)

    for f in os.listdir(REPO_ROOT):
        if f.startswith("calculator") and f.endswith(".py"):
            os.remove(os.path.join(REPO_ROOT, f))


def write_source_module(index, op):
    """Write a single-function source module."""
    lines = [f'"""Module {index}: arithmetic helper — {op}."""', ""]

    if op == "add":
        lines += [f"def add_{index}(a, b):", f"    return a + b", ""]
    elif op == "subtract":
        lines += [f"def subtract_{index}(a, b):", f"    return a - b", ""]
    elif op == "multiply":
        lines += [f"def multiply_{index}(a, b):", f"    return a * b", ""]
    elif op == "divide":
        lines += [f"def divide_{index}(a, b):", f"    if b == 0: raise ValueError('division by zero')", f"    return a / b", ""]
    elif op == "modulo":
        lines += [f"def modulo_{index}(a, b):", f"    return a % b", ""]
    elif op == "power":
        lines += [f"def power_{index}(a, b):", f"    return a ** b", ""]
    elif op == "min":
        lines += [f"def min_{index}(a, b):", f"    return a if a < b else b", ""]
    elif op == "max":
        lines += [f"def max_{index}(a, b):", f"    return a if a > b else b", ""]

    path = os.path.join(SRC_DIR, f"module_{index}.py")
    with open(path, "w") as f:
        f.write("\n".join(lines))


def write_test_file(test_index, src_indices, ops):
    """
    Write a test file that imports from 4 source modules.
    test_index: 1-based test file number
    src_indices: list of 4 source module indices this test imports from
    ops: list of 4 operations (one per source module)
    """
    imports = ", ".join(f"{ops[j]}_{src_indices[j]}" for j in range(MODULES_PER_TEST))
    src_imports = "\n".join(
        f"from module_{src_indices[j]} import {ops[j]}_{src_indices[j]}"
        for j in range(MODULES_PER_TEST)
    )

    lines = [
        f'"""Tests for test module {test_index} — covers src modules {src_indices}."""',
        f"import sys, os",
        f"sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))",
        src_imports,
        "",
    ]

    for j in range(MODULES_PER_TEST):
        idx = src_indices[j]
        op  = ops[j]
        fn  = f"{op}_{idx}"
        if op == "add":
            lines += [f"def test_{fn}():", f"    assert {fn}(2, 3) == 5", ""]
        elif op == "subtract":
            lines += [f"def test_{fn}():", f"    assert {fn}(10, 4) == 6", ""]
        elif op == "multiply":
            lines += [f"def test_{fn}():", f"    assert {fn}(3, 7) == 21", ""]
        elif op == "divide":
            lines += [f"def test_{fn}():", f"    assert {fn}(10, 2) == 5.0", ""]
        elif op == "modulo":
            lines += [f"def test_{fn}():", f"    assert {fn}(10, 3) == 1", ""]
        elif op == "power":
            lines += [f"def test_{fn}():", f"    assert {fn}(2, 8) == 256", ""]
        elif op == "min":
            lines += [f"def test_{fn}():", f"    assert {fn}(3, 7) == 3", ""]
        elif op == "max":
            lines += [f"def test_{fn}():", f"    assert {fn}(3, 7) == 7", ""]

    path = os.path.join(TESTS_DIR, f"test_module_{test_index}.py")
    with open(path, "w") as f:
        f.write("\n".join(lines))


def write_config(index):
    data = {
        "config_id": index,
        "name": f"service-config-{index}",
        "version": f"1.{index % 10}.{index % 5}",
        "enabled": index % 3 != 0,
        "timeout_ms": random.randint(100, 5000),
        "max_retries": random.randint(1, 10),
        "endpoints": [
            f"https://api-{index}.example.com/v1",
            f"https://api-{index}.example.com/v2",
        ],
        "feature_flags": {
            "enable_cache": index % 2 == 0,
            "enable_tracing": index % 5 == 0,
            "enable_metrics": True,
        },
        "tags": [f"env:prod", f"region:us-east-{index % 4}", f"team:platform"],
        "thresholds": {
            "cpu_pct": round(random.uniform(60, 95), 1),
            "mem_mb": random.randint(256, 4096),
            "rps": random.randint(100, 10000),
        },
    }
    path = os.path.join(CONFIGS_DIR, f"config_{index}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def write_conftest():
    with open(os.path.join(TESTS_DIR, "conftest.py"), "w") as f:
        f.write('"""Shared pytest configuration."""\n')


def write_gitignore():
    with open(os.path.join(REPO_ROOT, ".gitignore"), "w") as f:
        f.write(
            "__pycache__/\n*.pyc\n*.pyo\n.coverage\n*.egg-info/\n"
            "dist/\nbuild/\n.pytest_cache/\nreport.xml\n"
            ".harness_ti_env\n--report-paths/\n"
        )


def main():
    random.seed(42)

    print("Cleaning old directories...")
    clean_dirs()

    # Assign one operation per source module (cycling through OPERATIONS)
    ops_cycle = OPERATIONS * (NUM_SOURCE_FILES // len(OPERATIONS) + 1)

    print(f"Writing {NUM_SOURCE_FILES} source modules...")
    for i in range(1, NUM_SOURCE_FILES + 1):
        write_source_module(i, ops_cycle[i - 1])

    print(f"Writing {NUM_TEST_FILES} test files ({NUM_TEST_FILES * TESTS_PER_FILE} tests total)...")
    for t in range(1, NUM_TEST_FILES + 1):
        # Source modules for this test file: 4 consecutive starting at (t-1)*4 + 1
        base = (t - 1) * MODULES_PER_TEST + 1
        src_indices = list(range(base, base + MODULES_PER_TEST))
        test_ops = [ops_cycle[s - 1] for s in src_indices]
        write_test_file(t, src_indices, test_ops)

    print("Writing conftest.py...")
    write_conftest()

    print(f"Writing {NUM_CONFIGS} config files...")
    for i in range(1, NUM_CONFIGS + 1):
        write_config(i)

    print("Writing .gitignore...")
    write_gitignore()

    total_tests = NUM_TEST_FILES * TESTS_PER_FILE
    total_files = NUM_SOURCE_FILES + NUM_TEST_FILES + NUM_CONFIGS + 5  # +5 for root files
    print(f"\nDone!")
    print(f"  src/         {NUM_SOURCE_FILES} source modules")
    print(f"  tests/       {NUM_TEST_FILES} test files × {TESTS_PER_FILE} tests = {total_tests} total tests")
    print(f"  configs/     {NUM_CONFIGS} JSON config files")
    print(f"  Each test file imports from {MODULES_PER_TEST} source modules")
    print(f"  Estimated hash array size: ~{total_files} entries (vs ~606 on 1k branch)")


if __name__ == "__main__":
    main()
