"""Tests for test module 1097 — covers src modules [4385, 4386, 4387, 4388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4385 import add_4385
from module_4386 import subtract_4386
from module_4387 import multiply_4387
from module_4388 import divide_4388

def test_add_4385():
    assert add_4385(2, 3) == 5

def test_subtract_4386():
    assert subtract_4386(10, 4) == 6

def test_multiply_4387():
    assert multiply_4387(3, 7) == 21

def test_divide_4388():
    assert divide_4388(10, 2) == 5.0
