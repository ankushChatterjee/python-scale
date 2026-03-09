#!/usr/bin/env python3
"""
Generate a scale-test Python repo with:
  - 250 source modules (src/module_N.py)
  - 250 test files (tests/test_module_N.py), 4 tests each = 1000 tests total
  - 100 fake JSON config files (configs/config_N.json)
"""

import json
import os
import random
import shutil

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(REPO_ROOT, "src")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
CONFIGS_DIR = os.path.join(REPO_ROOT, "configs")

NUM_MODULES = 250
TESTS_PER_FILE = 4  # 250 * 4 = 1000 tests
NUM_CONFIGS = 100

OPERATIONS = ["add", "subtract", "multiply", "divide", "modulo", "power", "min", "max"]


def clean_dirs():
    for d in [SRC_DIR, TESTS_DIR, CONFIGS_DIR]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)

    # Remove old calculator*.py files from root
    for f in os.listdir(REPO_ROOT):
        if f.startswith("calculator") and f.endswith(".py"):
            os.remove(os.path.join(REPO_ROOT, f))


def write_source_module(index):
    ops = random.sample(OPERATIONS, TESTS_PER_FILE)
    lines = [
        f'"""Module {index}: arithmetic helpers."""',
        "",
    ]
    for op in ops:
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
    return ops


def write_test_file(index, ops):
    lines = [
        f'"""Tests for module {index}."""',
        f"import sys, os",
        f"sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))",
        f"from module_{index} import " + ", ".join(f"{op}_{index}" for op in ops),
        "",
    ]
    for op in ops:
        fn = f"{op}_{index}"
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

    path = os.path.join(TESTS_DIR, f"test_module_{index}.py")
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
    path = os.path.join(TESTS_DIR, "conftest.py")
    with open(path, "w") as f:
        f.write('"""Shared pytest configuration."""\n')


def write_gitignore():
    path = os.path.join(REPO_ROOT, ".gitignore")
    with open(path, "w") as f:
        f.write("__pycache__/\n*.pyc\n*.pyo\n.coverage\n*.egg-info/\ndist/\nbuild/\n.pytest_cache/\nreport.xml\n")


def main():
    random.seed(42)  # reproducible

    print("Cleaning old directories...")
    clean_dirs()

    print(f"Writing {NUM_MODULES} source modules...")
    for i in range(1, NUM_MODULES + 1):
        ops = write_source_module(i)
        write_test_file(i, ops)

    print(f"Writing conftest.py...")
    write_conftest()

    print(f"Writing {NUM_CONFIGS} config files...")
    for i in range(1, NUM_CONFIGS + 1):
        write_config(i)

    print(f"Writing .gitignore...")
    write_gitignore()

    total_tests = NUM_MODULES * TESTS_PER_FILE
    print(f"\nDone!")
    print(f"  src/         {NUM_MODULES} Python modules")
    print(f"  tests/       {NUM_MODULES} test files x {TESTS_PER_FILE} tests = {total_tests} total tests")
    print(f"  configs/     {NUM_CONFIGS} JSON config files")


if __name__ == "__main__":
    main()
