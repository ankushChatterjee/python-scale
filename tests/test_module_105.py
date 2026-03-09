"""Tests for test module 105 — covers src modules [417, 418, 419, 420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_417 import add_417
from module_418 import subtract_418
from module_419 import multiply_419
from module_420 import divide_420

def test_add_417():
    assert add_417(2, 3) == 5

def test_subtract_418():
    assert subtract_418(10, 4) == 6

def test_multiply_419():
    assert multiply_419(3, 7) == 21

def test_divide_420():
    assert divide_420(10, 2) == 5.0
