"""Tests for test module 553 — covers src modules [2209, 2210, 2211, 2212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2209 import add_2209
from module_2210 import subtract_2210
from module_2211 import multiply_2211
from module_2212 import divide_2212

def test_add_2209():
    assert add_2209(2, 3) == 5

def test_subtract_2210():
    assert subtract_2210(10, 4) == 6

def test_multiply_2211():
    assert multiply_2211(3, 7) == 21

def test_divide_2212():
    assert divide_2212(10, 2) == 5.0
