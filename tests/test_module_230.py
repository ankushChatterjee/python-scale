"""Tests for module 230."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_230 import divide_230, power_230, subtract_230, multiply_230

def test_divide_230():
    assert divide_230(10, 2) == 5.0

def test_power_230():
    assert power_230(2, 8) == 256

def test_subtract_230():
    assert subtract_230(10, 4) == 6

def test_multiply_230():
    assert multiply_230(3, 7) == 21
