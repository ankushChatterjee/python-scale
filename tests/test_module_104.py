"""Tests for test module 104 — covers src modules [413, 414, 415, 416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_413 import modulo_413
from module_414 import power_414
from module_415 import min_415
from module_416 import max_416

def test_modulo_413():
    assert modulo_413(10, 3) == 1

def test_power_414():
    assert power_414(2, 8) == 256

def test_min_415():
    assert min_415(3, 7) == 3

def test_max_416():
    assert max_416(3, 7) == 7
