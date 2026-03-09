"""Tests for test module 2097 — covers src modules [8385, 8386, 8387, 8388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8385 import add_8385
from module_8386 import subtract_8386
from module_8387 import multiply_8387
from module_8388 import divide_8388

def test_add_8385():
    assert add_8385(2, 3) == 5

def test_subtract_8386():
    assert subtract_8386(10, 4) == 6

def test_multiply_8387():
    assert multiply_8387(3, 7) == 21

def test_divide_8388():
    assert divide_8388(10, 2) == 5.0
