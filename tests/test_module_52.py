"""Tests for module 52."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_52 import divide_52, add_52, min_52, power_52

def test_divide_52():
    assert divide_52(10, 2) == 5.0

def test_add_52():
    assert add_52(2, 3) == 5

def test_min_52():
    assert min_52(3, 7) == 3

def test_power_52():
    assert power_52(2, 8) == 256
