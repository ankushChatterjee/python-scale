"""Tests for test module 1563 — covers src modules [6249, 6250, 6251, 6252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6249 import add_6249
from module_6250 import subtract_6250
from module_6251 import multiply_6251
from module_6252 import divide_6252

def test_add_6249():
    assert add_6249(2, 3) == 5

def test_subtract_6250():
    assert subtract_6250(10, 4) == 6

def test_multiply_6251():
    assert multiply_6251(3, 7) == 21

def test_divide_6252():
    assert divide_6252(10, 2) == 5.0
