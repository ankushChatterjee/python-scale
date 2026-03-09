"""Tests for test module 53 — covers src modules [209, 210, 211, 212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_209 import add_209
from module_210 import subtract_210
from module_211 import multiply_211
from module_212 import divide_212

def test_add_209():
    assert add_209(2, 3) == 5

def test_subtract_210():
    assert subtract_210(10, 4) == 6

def test_multiply_211():
    assert multiply_211(3, 7) == 21

def test_divide_212():
    assert divide_212(10, 2) == 5.0
