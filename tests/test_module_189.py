"""Tests for module 189."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_189 import power_189, subtract_189, divide_189, min_189

def test_power_189():
    assert power_189(2, 8) == 256

def test_subtract_189():
    assert subtract_189(10, 4) == 6

def test_divide_189():
    assert divide_189(10, 2) == 5.0

def test_min_189():
    assert min_189(3, 7) == 3
