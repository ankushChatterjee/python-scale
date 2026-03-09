"""Tests for module 149."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_149 import subtract_149, max_149, min_149, power_149

def test_subtract_149():
    assert subtract_149(10, 4) == 6

def test_max_149():
    assert max_149(3, 7) == 7

def test_min_149():
    assert min_149(3, 7) == 3

def test_power_149():
    assert power_149(2, 8) == 256
