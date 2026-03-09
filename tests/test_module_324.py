"""Tests for test module 324 — covers src modules [1293, 1294, 1295, 1296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1293 import modulo_1293
from module_1294 import power_1294
from module_1295 import min_1295
from module_1296 import max_1296

def test_modulo_1293():
    assert modulo_1293(10, 3) == 1

def test_power_1294():
    assert power_1294(2, 8) == 256

def test_min_1295():
    assert min_1295(3, 7) == 3

def test_max_1296():
    assert max_1296(3, 7) == 7
