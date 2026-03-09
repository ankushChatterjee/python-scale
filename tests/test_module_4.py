"""Tests for module 4."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4 import add_4, max_4, subtract_4, power_4

def test_add_4():
    assert add_4(2, 3) == 5

def test_max_4():
    assert max_4(3, 7) == 7

def test_subtract_4():
    assert subtract_4(10, 4) == 6

def test_power_4():
    assert power_4(2, 8) == 256
