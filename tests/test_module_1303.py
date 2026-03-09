"""Tests for test module 1303 — covers src modules [5209, 5210, 5211, 5212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5209 import add_5209
from module_5210 import subtract_5210
from module_5211 import multiply_5211
from module_5212 import divide_5212

def test_add_5209():
    assert add_5209(2, 3) == 5

def test_subtract_5210():
    assert subtract_5210(10, 4) == 6

def test_multiply_5211():
    assert multiply_5211(3, 7) == 21

def test_divide_5212():
    assert divide_5212(10, 2) == 5.0
