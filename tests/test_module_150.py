"""Tests for module 150."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_150 import min_150, power_150, subtract_150, max_150

def test_min_150():
    assert min_150(3, 7) == 3

def test_power_150():
    assert power_150(2, 8) == 256

def test_subtract_150():
    assert subtract_150(10, 4) == 6

def test_max_150():
    assert max_150(3, 7) == 7
