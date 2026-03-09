"""Tests for module 31."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_31 import multiply_31, power_31, subtract_31, divide_31

def test_multiply_31():
    assert multiply_31(3, 7) == 21

def test_power_31():
    assert power_31(2, 8) == 256

def test_subtract_31():
    assert subtract_31(10, 4) == 6

def test_divide_31():
    assert divide_31(10, 2) == 5.0
