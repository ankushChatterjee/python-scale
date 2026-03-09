"""Tests for test module 770 — covers src modules [3077, 3078, 3079, 3080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3077 import modulo_3077
from module_3078 import power_3078
from module_3079 import min_3079
from module_3080 import max_3080

def test_modulo_3077():
    assert modulo_3077(10, 3) == 1

def test_power_3078():
    assert power_3078(2, 8) == 256

def test_min_3079():
    assert min_3079(3, 7) == 3

def test_max_3080():
    assert max_3080(3, 7) == 7
