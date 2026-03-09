"""Tests for test module 303 — covers src modules [1209, 1210, 1211, 1212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1209 import add_1209
from module_1210 import subtract_1210
from module_1211 import multiply_1211
from module_1212 import divide_1212

def test_add_1209():
    assert add_1209(2, 3) == 5

def test_subtract_1210():
    assert subtract_1210(10, 4) == 6

def test_multiply_1211():
    assert multiply_1211(3, 7) == 21

def test_divide_1212():
    assert divide_1212(10, 2) == 5.0
