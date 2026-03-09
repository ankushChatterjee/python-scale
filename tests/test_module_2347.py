"""Tests for test module 2347 — covers src modules [9385, 9386, 9387, 9388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9385 import add_9385
from module_9386 import subtract_9386
from module_9387 import multiply_9387
from module_9388 import divide_9388

def test_add_9385():
    assert add_9385(2, 3) == 5

def test_subtract_9386():
    assert subtract_9386(10, 4) == 6

def test_multiply_9387():
    assert multiply_9387(3, 7) == 21

def test_divide_9388():
    assert divide_9388(10, 2) == 5.0
