"""Tests for module 66."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_66 import subtract_66, min_66, max_66, power_66

def test_subtract_66():
    assert subtract_66(10, 4) == 6

def test_min_66():
    assert min_66(3, 7) == 3

def test_max_66():
    assert max_66(3, 7) == 7

def test_power_66():
    assert power_66(2, 8) == 256
