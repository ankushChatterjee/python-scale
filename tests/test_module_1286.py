"""Tests for test module 1286 — covers src modules [5141, 5142, 5143, 5144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5141 import modulo_5141
from module_5142 import power_5142
from module_5143 import min_5143
from module_5144 import max_5144

def test_modulo_5141():
    assert modulo_5141(10, 3) == 1

def test_power_5142():
    assert power_5142(2, 8) == 256

def test_min_5143():
    assert min_5143(3, 7) == 3

def test_max_5144():
    assert max_5144(3, 7) == 7
