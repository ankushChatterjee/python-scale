"""Tests for test module 855 — covers src modules [3417, 3418, 3419, 3420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3417 import add_3417
from module_3418 import subtract_3418
from module_3419 import multiply_3419
from module_3420 import divide_3420

def test_add_3417():
    assert add_3417(2, 3) == 5

def test_subtract_3418():
    assert subtract_3418(10, 4) == 6

def test_multiply_3419():
    assert multiply_3419(3, 7) == 21

def test_divide_3420():
    assert divide_3420(10, 2) == 5.0
