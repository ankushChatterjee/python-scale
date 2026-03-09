"""Tests for test module 23 — covers src modules [89, 90, 91, 92]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_89 import add_89
from module_90 import subtract_90
from module_91 import multiply_91
from module_92 import divide_92

def test_add_89():
    assert add_89(2, 3) == 5

def test_subtract_90():
    assert subtract_90(10, 4) == 6

def test_multiply_91():
    assert multiply_91(3, 7) == 21

def test_divide_92():
    assert divide_92(10, 2) == 5.0
