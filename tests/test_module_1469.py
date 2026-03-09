"""Tests for test module 1469 — covers src modules [5873, 5874, 5875, 5876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5873 import add_5873
from module_5874 import subtract_5874
from module_5875 import multiply_5875
from module_5876 import divide_5876

def test_add_5873():
    assert add_5873(2, 3) == 5

def test_subtract_5874():
    assert subtract_5874(10, 4) == 6

def test_multiply_5875():
    assert multiply_5875(3, 7) == 21

def test_divide_5876():
    assert divide_5876(10, 2) == 5.0
