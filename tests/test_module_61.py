"""Tests for module 61."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_61 import subtract_61, max_61, min_61, power_61

def test_subtract_61():
    assert subtract_61(10, 4) == 6

def test_max_61():
    assert max_61(3, 7) == 7

def test_min_61():
    assert min_61(3, 7) == 3

def test_power_61():
    assert power_61(2, 8) == 256
