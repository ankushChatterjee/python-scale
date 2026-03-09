"""Tests for test module 1855 — covers src modules [7417, 7418, 7419, 7420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7417 import add_7417
from module_7418 import subtract_7418
from module_7419 import multiply_7419
from module_7420 import divide_7420

def test_add_7417():
    assert add_7417(2, 3) == 5

def test_subtract_7418():
    assert subtract_7418(10, 4) == 6

def test_multiply_7419():
    assert multiply_7419(3, 7) == 21

def test_divide_7420():
    assert divide_7420(10, 2) == 5.0
