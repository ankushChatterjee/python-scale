"""Tests for module 132."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_132 import power_132, add_132, subtract_132, multiply_132

def test_power_132():
    assert power_132(2, 8) == 256

def test_add_132():
    assert add_132(2, 3) == 5

def test_subtract_132():
    assert subtract_132(10, 4) == 6

def test_multiply_132():
    assert multiply_132(3, 7) == 21
