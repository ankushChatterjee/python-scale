"""Tests for module 106."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_106 import min_106, max_106, power_106, subtract_106

def test_min_106():
    assert min_106(3, 7) == 3

def test_max_106():
    assert max_106(3, 7) == 7

def test_power_106():
    assert power_106(2, 8) == 256

def test_subtract_106():
    assert subtract_106(10, 4) == 6
