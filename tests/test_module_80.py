"""Tests for module 80."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_80 import power_80, multiply_80, subtract_80, min_80

def test_power_80():
    assert power_80(2, 8) == 256

def test_multiply_80():
    assert multiply_80(3, 7) == 21

def test_subtract_80():
    assert subtract_80(10, 4) == 6

def test_min_80():
    assert min_80(3, 7) == 3
