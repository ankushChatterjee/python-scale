"""Tests for test module 1347 — covers src modules [5385, 5386, 5387, 5388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5385 import add_5385
from module_5386 import subtract_5386
from module_5387 import multiply_5387
from module_5388 import divide_5388

def test_add_5385():
    assert add_5385(2, 3) == 5

def test_subtract_5386():
    assert subtract_5386(10, 4) == 6

def test_multiply_5387():
    assert multiply_5387(3, 7) == 21

def test_divide_5388():
    assert divide_5388(10, 2) == 5.0
