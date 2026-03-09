"""Tests for test module 1270 — covers src modules [5077, 5078, 5079, 5080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5077 import modulo_5077
from module_5078 import power_5078
from module_5079 import min_5079
from module_5080 import max_5080

def test_modulo_5077():
    assert modulo_5077(10, 3) == 1

def test_power_5078():
    assert power_5078(2, 8) == 256

def test_min_5079():
    assert min_5079(3, 7) == 3

def test_max_5080():
    assert max_5080(3, 7) == 7
