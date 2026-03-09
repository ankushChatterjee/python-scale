"""Tests for test module 270 — covers src modules [1077, 1078, 1079, 1080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1077 import modulo_1077
from module_1078 import power_1078
from module_1079 import min_1079
from module_1080 import max_1080

def test_modulo_1077():
    assert modulo_1077(10, 3) == 1

def test_power_1078():
    assert power_1078(2, 8) == 256

def test_min_1079():
    assert min_1079(3, 7) == 3

def test_max_1080():
    assert max_1080(3, 7) == 7
