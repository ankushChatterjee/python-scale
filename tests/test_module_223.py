"""Tests for module 223."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_223 import subtract_223, max_223, min_223, power_223

def test_subtract_223():
    assert subtract_223(10, 4) == 6

def test_max_223():
    assert max_223(3, 7) == 7

def test_min_223():
    assert min_223(3, 7) == 3

def test_power_223():
    assert power_223(2, 8) == 256
