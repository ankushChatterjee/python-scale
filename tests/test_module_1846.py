"""Tests for test module 1846 — covers src modules [7381, 7382, 7383, 7384]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7381 import modulo_7381
from module_7382 import power_7382
from module_7383 import min_7383
from module_7384 import max_7384

def test_modulo_7381():
    assert modulo_7381(10, 3) == 1

def test_power_7382():
    assert power_7382(2, 8) == 256

def test_min_7383():
    assert min_7383(3, 7) == 3

def test_max_7384():
    assert max_7384(3, 7) == 7
