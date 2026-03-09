"""Tests for module 60."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_60 import add_60, divide_60, power_60, multiply_60

def test_add_60():
    assert add_60(2, 3) == 5

def test_divide_60():
    assert divide_60(10, 2) == 5.0

def test_power_60():
    assert power_60(2, 8) == 256

def test_multiply_60():
    assert multiply_60(3, 7) == 21
