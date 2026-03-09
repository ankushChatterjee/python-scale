"""Tests for module 134."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_134 import add_134, max_134, subtract_134, divide_134

def test_add_134():
    assert add_134(2, 3) == 5

def test_max_134():
    assert max_134(3, 7) == 7

def test_subtract_134():
    assert subtract_134(10, 4) == 6

def test_divide_134():
    assert divide_134(10, 2) == 5.0
