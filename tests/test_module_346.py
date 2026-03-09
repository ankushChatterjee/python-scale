"""Tests for test module 346 — covers src modules [1381, 1382, 1383, 1384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1381 import modulo_1381
from module_1382 import power_1382
from module_1383 import min_1383
from module_1384 import max_1384

def test_modulo_1381():
    assert modulo_1381(10, 3) == 1

def test_power_1382():
    assert power_1382(2, 8) == 256

def test_min_1383():
    assert min_1383(3, 7) == 3

def test_max_1384():
    assert max_1384(3, 7) == 7
