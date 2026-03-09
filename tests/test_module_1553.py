"""Tests for test module 1553 — covers src modules [6209, 6210, 6211, 6212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6209 import add_6209
from module_6210 import subtract_6210
from module_6211 import multiply_6211
from module_6212 import divide_6212

def test_add_6209():
    assert add_6209(2, 3) == 5

def test_subtract_6210():
    assert subtract_6210(10, 4) == 6

def test_multiply_6211():
    assert multiply_6211(3, 7) == 21

def test_divide_6212():
    assert divide_6212(10, 2) == 5.0
