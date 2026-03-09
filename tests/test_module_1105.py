"""Tests for test module 1105 — covers src modules [4417, 4418, 4419, 4420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4417 import add_4417
from module_4418 import subtract_4418
from module_4419 import multiply_4419
from module_4420 import divide_4420

def test_add_4417():
    assert add_4417(2, 3) == 5

def test_subtract_4418():
    assert subtract_4418(10, 4) == 6

def test_multiply_4419():
    assert multiply_4419(3, 7) == 21

def test_divide_4420():
    assert divide_4420(10, 2) == 5.0
