"""Tests for test module 97 — covers src modules [385, 386, 387, 388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_385 import add_385
from module_386 import subtract_386
from module_387 import multiply_387
from module_388 import divide_388

def test_add_385():
    assert add_385(2, 3) == 5

def test_subtract_386():
    assert subtract_386(10, 4) == 6

def test_multiply_387():
    assert multiply_387(3, 7) == 21

def test_divide_388():
    assert divide_388(10, 2) == 5.0
