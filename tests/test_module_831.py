"""Tests for test module 831 — covers src modules [3321, 3322, 3323, 3324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3321 import add_3321
from module_3322 import subtract_3322
from module_3323 import multiply_3323
from module_3324 import divide_3324

def test_add_3321():
    assert add_3321(2, 3) == 5

def test_subtract_3322():
    assert subtract_3322(10, 4) == 6

def test_multiply_3323():
    assert multiply_3323(3, 7) == 21

def test_divide_3324():
    assert divide_3324(10, 2) == 5.0
