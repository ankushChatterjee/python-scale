"""Tests for test module 2270 — covers src modules [9077, 9078, 9079, 9080]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9077 import modulo_9077
from module_9078 import power_9078
from module_9079 import min_9079
from module_9080 import max_9080

def test_modulo_9077():
    assert modulo_9077(10, 3) == 1

def test_power_9078():
    assert power_9078(2, 8) == 256

def test_min_9079():
    assert min_9079(3, 7) == 3

def test_max_9080():
    assert max_9080(3, 7) == 7
