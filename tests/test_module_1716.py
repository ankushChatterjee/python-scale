"""Tests for test module 1716 — covers src modules [6861, 6862, 6863, 6864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6861 import modulo_6861
from module_6862 import power_6862
from module_6863 import min_6863
from module_6864 import max_6864

def test_modulo_6861():
    assert modulo_6861(10, 3) == 1

def test_power_6862():
    assert power_6862(2, 8) == 256

def test_min_6863():
    assert min_6863(3, 7) == 3

def test_max_6864():
    assert max_6864(3, 7) == 7
