"""Tests for module 26."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_26 import min_26, power_26, divide_26, subtract_26

def test_min_26():
    assert min_26(3, 7) == 3

def test_power_26():
    assert power_26(2, 8) == 256

def test_divide_26():
    assert divide_26(10, 2) == 5.0

def test_subtract_26():
    assert subtract_26(10, 4) == 6
