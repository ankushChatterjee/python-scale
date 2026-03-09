"""Tests for test module 711 — covers src modules [2841, 2842, 2843, 2844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2841 import add_2841
from module_2842 import subtract_2842
from module_2843 import multiply_2843
from module_2844 import divide_2844

def test_add_2841():
    assert add_2841(2, 3) == 5

def test_subtract_2842():
    assert subtract_2842(10, 4) == 6

def test_multiply_2843():
    assert multiply_2843(3, 7) == 21

def test_divide_2844():
    assert divide_2844(10, 2) == 5.0
