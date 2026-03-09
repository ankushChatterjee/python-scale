"""Tests for module 102."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_102 import divide_102, power_102, subtract_102, add_102

def test_divide_102():
    assert divide_102(10, 2) == 5.0

def test_power_102():
    assert power_102(2, 8) == 256

def test_subtract_102():
    assert subtract_102(10, 4) == 6

def test_add_102():
    assert add_102(2, 3) == 5
