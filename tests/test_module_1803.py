"""Tests for test module 1803 — covers src modules [7209, 7210, 7211, 7212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7209 import add_7209
from module_7210 import subtract_7210
from module_7211 import multiply_7211
from module_7212 import divide_7212

def test_add_7209():
    assert add_7209(2, 3) == 5

def test_subtract_7210():
    assert subtract_7210(10, 4) == 6

def test_multiply_7211():
    assert multiply_7211(3, 7) == 21

def test_divide_7212():
    assert divide_7212(10, 2) == 5.0
