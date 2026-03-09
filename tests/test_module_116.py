"""Tests for test module 116 — covers src modules [461, 462, 463, 464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_461 import modulo_461
from module_462 import power_462
from module_463 import min_463
from module_464 import max_464

def test_modulo_461():
    assert modulo_461(10, 3) == 1

def test_power_462():
    assert power_462(2, 8) == 256

def test_min_463():
    assert min_463(3, 7) == 3

def test_max_464():
    assert max_464(3, 7) == 7
