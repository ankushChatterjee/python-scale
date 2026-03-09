"""Tests for test module 1605 — covers src modules [6417, 6418, 6419, 6420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6417 import add_6417
from module_6418 import subtract_6418
from module_6419 import multiply_6419
from module_6420 import divide_6420

def test_add_6417():
    assert add_6417(2, 3) == 5

def test_subtract_6418():
    assert subtract_6418(10, 4) == 6

def test_multiply_6419():
    assert multiply_6419(3, 7) == 21

def test_divide_6420():
    assert divide_6420(10, 2) == 5.0
