"""Tests for module 14."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_14 import power_14, modulo_14, subtract_14, add_14

def test_power_14():
    assert power_14(2, 8) == 256

def test_modulo_14():
    assert modulo_14(10, 3) == 1

def test_subtract_14():
    assert subtract_14(10, 4) == 6

def test_add_14():
    assert add_14(2, 3) == 5
