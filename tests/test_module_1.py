"""Tests for module 1."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1 import subtract_1, add_1, power_1, multiply_1

def test_subtract_1():
    assert subtract_1(10, 4) == 6

def test_add_1():
    assert add_1(2, 3) == 5

def test_power_1():
    assert power_1(2, 8) == 256

def test_multiply_1():
    assert multiply_1(3, 7) == 21
