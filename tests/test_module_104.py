"""Tests for module 104."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_104 import multiply_104, subtract_104, min_104, power_104

def test_multiply_104():
    assert multiply_104(3, 7) == 21

def test_subtract_104():
    assert subtract_104(10, 4) == 6

def test_min_104():
    assert min_104(3, 7) == 3

def test_power_104():
    assert power_104(2, 8) == 256
