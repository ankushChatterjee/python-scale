"""Tests for test module 1597 — covers src modules [6385, 6386, 6387, 6388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6385 import add_6385
from module_6386 import subtract_6386
from module_6387 import multiply_6387
from module_6388 import divide_6388

def test_add_6385():
    assert add_6385(2, 3) == 5

def test_subtract_6386():
    assert subtract_6386(10, 4) == 6

def test_multiply_6387():
    assert multiply_6387(3, 7) == 21

def test_divide_6388():
    assert divide_6388(10, 2) == 5.0
