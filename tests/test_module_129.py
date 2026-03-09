"""Tests for module 129."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_129 import power_129, divide_129, min_129, max_129

def test_power_129():
    assert power_129(2, 8) == 256

def test_divide_129():
    assert divide_129(10, 2) == 5.0

def test_min_129():
    assert min_129(3, 7) == 3

def test_max_129():
    assert max_129(3, 7) == 7
