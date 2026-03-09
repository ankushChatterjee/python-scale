"""Tests for module 15."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_15 import add_15, power_15, subtract_15, multiply_15

def test_add_15():
    assert add_15(2, 3) == 5

def test_power_15():
    assert power_15(2, 8) == 256

def test_subtract_15():
    assert subtract_15(10, 4) == 6

def test_multiply_15():
    assert multiply_15(3, 7) == 21
