"""Tests for test module 1581 — covers src modules [6321, 6322, 6323, 6324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6321 import add_6321
from module_6322 import subtract_6322
from module_6323 import multiply_6323
from module_6324 import divide_6324

def test_add_6321():
    assert add_6321(2, 3) == 5

def test_subtract_6322():
    assert subtract_6322(10, 4) == 6

def test_multiply_6323():
    assert multiply_6323(3, 7) == 21

def test_divide_6324():
    assert divide_6324(10, 2) == 5.0
