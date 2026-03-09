"""Tests for module 138."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_138 import add_138, min_138, max_138, divide_138

def test_add_138():
    assert add_138(2, 3) == 5

def test_min_138():
    assert min_138(3, 7) == 3

def test_max_138():
    assert max_138(3, 7) == 7

def test_divide_138():
    assert divide_138(10, 2) == 5.0
