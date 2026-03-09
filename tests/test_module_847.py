"""Tests for test module 847 — covers src modules [3385, 3386, 3387, 3388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3385 import add_3385
from module_3386 import subtract_3386
from module_3387 import multiply_3387
from module_3388 import divide_3388

def test_add_3385():
    assert add_3385(2, 3) == 5

def test_subtract_3386():
    assert subtract_3386(10, 4) == 6

def test_multiply_3387():
    assert multiply_3387(3, 7) == 21

def test_divide_3388():
    assert divide_3388(10, 2) == 5.0
