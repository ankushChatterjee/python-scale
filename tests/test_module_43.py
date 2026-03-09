"""Tests for module 43."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_43 import subtract_43, add_43, power_43, divide_43

def test_subtract_43():
    assert subtract_43(10, 4) == 6

def test_add_43():
    assert add_43(2, 3) == 5

def test_power_43():
    assert power_43(2, 8) == 256

def test_divide_43():
    assert divide_43(10, 2) == 5.0
