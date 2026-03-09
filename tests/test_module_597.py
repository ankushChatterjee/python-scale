"""Tests for test module 597 — covers src modules [2385, 2386, 2387, 2388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2385 import add_2385
from module_2386 import subtract_2386
from module_2387 import multiply_2387
from module_2388 import divide_2388

def test_add_2385():
    assert add_2385(2, 3) == 5

def test_subtract_2386():
    assert subtract_2386(10, 4) == 6

def test_multiply_2387():
    assert multiply_2387(3, 7) == 21

def test_divide_2388():
    assert divide_2388(10, 2) == 5.0
