"""Tests for test module 2105 — covers src modules [8417, 8418, 8419, 8420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8417 import add_8417
from module_8418 import subtract_8418
from module_8419 import multiply_8419
from module_8420 import divide_8420

def test_add_8417():
    assert add_8417(2, 3) == 5

def test_subtract_8418():
    assert subtract_8418(10, 4) == 6

def test_multiply_8419():
    assert multiply_8419(3, 7) == 21

def test_divide_8420():
    assert divide_8420(10, 2) == 5.0
