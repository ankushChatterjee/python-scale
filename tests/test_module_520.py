"""Tests for test module 520 — covers src modules [2077, 2078, 2079, 2080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2077 import modulo_2077
from module_2078 import power_2078
from module_2079 import min_2079
from module_2080 import max_2080

def test_modulo_2077():
    assert modulo_2077(10, 3) == 1

def test_power_2078():
    assert power_2078(2, 8) == 256

def test_min_2079():
    assert min_2079(3, 7) == 3

def test_max_2080():
    assert max_2080(3, 7) == 7
