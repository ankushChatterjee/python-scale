"""Tests for test module 1847 — covers src modules [7385, 7386, 7387, 7388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7385 import add_7385
from module_7386 import subtract_7386
from module_7387 import multiply_7387
from module_7388 import divide_7388

def test_add_7385():
    assert add_7385(2, 3) == 5

def test_subtract_7386():
    assert subtract_7386(10, 4) == 6

def test_multiply_7387():
    assert multiply_7387(3, 7) == 21

def test_divide_7388():
    assert divide_7388(10, 2) == 5.0
