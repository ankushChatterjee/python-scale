"""Tests for test module 2199 — covers src modules [8793, 8794, 8795, 8796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8793 import add_8793
from module_8794 import subtract_8794
from module_8795 import multiply_8795
from module_8796 import divide_8796

def test_add_8793():
    assert add_8793(2, 3) == 5

def test_subtract_8794():
    assert subtract_8794(10, 4) == 6

def test_multiply_8795():
    assert multiply_8795(3, 7) == 21

def test_divide_8796():
    assert divide_8796(10, 2) == 5.0
