"""Tests for module 222."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_222 import divide_222, power_222, subtract_222, multiply_222

def test_divide_222():
    assert divide_222(10, 2) == 5.0

def test_power_222():
    assert power_222(2, 8) == 256

def test_subtract_222():
    assert subtract_222(10, 4) == 6

def test_multiply_222():
    assert multiply_222(3, 7) == 21
