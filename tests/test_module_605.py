"""Tests for test module 605 — covers src modules [2417, 2418, 2419, 2420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2417 import add_2417
from module_2418 import subtract_2418
from module_2419 import multiply_2419
from module_2420 import divide_2420

def test_add_2417():
    assert add_2417(2, 3) == 5

def test_subtract_2418():
    assert subtract_2418(10, 4) == 6

def test_multiply_2419():
    assert multiply_2419(3, 7) == 21

def test_divide_2420():
    assert divide_2420(10, 2) == 5.0
