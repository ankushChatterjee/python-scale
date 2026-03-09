"""Tests for module 25."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_25 import power_25, subtract_25, max_25, divide_25

def test_power_25():
    assert power_25(2, 8) == 256

def test_subtract_25():
    assert subtract_25(10, 4) == 6

def test_max_25():
    assert max_25(3, 7) == 7

def test_divide_25():
    assert divide_25(10, 2) == 5.0
