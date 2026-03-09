"""Tests for test module 1053 — covers src modules [4209, 4210, 4211, 4212]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4209 import add_4209
from module_4210 import subtract_4210
from module_4211 import multiply_4211
from module_4212 import divide_4212

def test_add_4209():
    assert add_4209(2, 3) == 5

def test_subtract_4210():
    assert subtract_4210(10, 4) == 6

def test_multiply_4211():
    assert multiply_4211(3, 7) == 21

def test_divide_4212():
    assert divide_4212(10, 2) == 5.0
