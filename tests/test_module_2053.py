"""Tests for test module 2053 — covers src modules [8209, 8210, 8211, 8212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8209 import add_8209
from module_8210 import subtract_8210
from module_8211 import multiply_8211
from module_8212 import divide_8212

def test_add_8209():
    assert add_8209(2, 3) == 5

def test_subtract_8210():
    assert subtract_8210(10, 4) == 6

def test_multiply_8211():
    assert multiply_8211(3, 7) == 21

def test_divide_8212():
    assert divide_8212(10, 2) == 5.0
