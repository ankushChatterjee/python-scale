"""Tests for test module 253 — covers src modules [1009, 1010, 1011, 1012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1009 import add_1009
from module_1010 import subtract_1010
from module_1011 import multiply_1011
from module_1012 import divide_1012

def test_add_1009():
    assert add_1009(2, 3) == 5

def test_subtract_1010():
    assert subtract_1010(10, 4) == 6

def test_multiply_1011():
    assert multiply_1011(3, 7) == 21

def test_divide_1012():
    assert divide_1012(10, 2) == 5.0
