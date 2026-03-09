"""Tests for module 58."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_58 import power_58, divide_58, min_58, max_58

def test_power_58():
    assert power_58(2, 8) == 256

def test_divide_58():
    assert divide_58(10, 2) == 5.0

def test_min_58():
    assert min_58(3, 7) == 3

def test_max_58():
    assert max_58(3, 7) == 7
