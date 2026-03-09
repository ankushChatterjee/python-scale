"""Tests for test module 1813 — covers src modules [7249, 7250, 7251, 7252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7249 import add_7249
from module_7250 import subtract_7250
from module_7251 import multiply_7251
from module_7252 import divide_7252

def test_add_7249():
    assert add_7249(2, 3) == 5

def test_subtract_7250():
    assert subtract_7250(10, 4) == 6

def test_multiply_7251():
    assert multiply_7251(3, 7) == 21

def test_divide_7252():
    assert divide_7252(10, 2) == 5.0
