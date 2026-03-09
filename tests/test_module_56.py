"""Tests for module 56."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_56 import max_56, subtract_56, divide_56, power_56

def test_max_56():
    assert max_56(3, 7) == 7

def test_subtract_56():
    assert subtract_56(10, 4) == 6

def test_divide_56():
    assert divide_56(10, 2) == 5.0

def test_power_56():
    assert power_56(2, 8) == 256
