"""Tests for module 111."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_111 import add_111, power_111, subtract_111, divide_111

def test_add_111():
    assert add_111(2, 3) == 5

def test_power_111():
    assert power_111(2, 8) == 256

def test_subtract_111():
    assert subtract_111(10, 4) == 6

def test_divide_111():
    assert divide_111(10, 2) == 5.0
