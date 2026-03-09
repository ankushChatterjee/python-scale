"""Tests for test module 1770 — covers src modules [7077, 7078, 7079, 7080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7077 import modulo_7077
from module_7078 import power_7078
from module_7079 import min_7079
from module_7080 import max_7080

def test_modulo_7077():
    assert modulo_7077(10, 3) == 1

def test_power_7078():
    assert power_7078(2, 8) == 256

def test_min_7079():
    assert min_7079(3, 7) == 3

def test_max_7080():
    assert max_7080(3, 7) == 7
