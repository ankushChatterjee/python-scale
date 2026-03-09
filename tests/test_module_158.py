"""Tests for module 158."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_158 import power_158, max_158, min_158, divide_158

def test_power_158():
    assert power_158(2, 8) == 256

def test_max_158():
    assert max_158(3, 7) == 7

def test_min_158():
    assert min_158(3, 7) == 3

def test_divide_158():
    assert divide_158(10, 2) == 5.0
