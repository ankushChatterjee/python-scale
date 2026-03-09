"""Tests for module 125."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_125 import multiply_125, subtract_125, divide_125, power_125

def test_multiply_125():
    assert multiply_125(3, 7) == 21

def test_subtract_125():
    assert subtract_125(10, 4) == 6

def test_divide_125():
    assert divide_125(10, 2) == 5.0

def test_power_125():
    assert power_125(2, 8) == 256
