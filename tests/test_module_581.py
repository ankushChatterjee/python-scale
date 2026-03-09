"""Tests for test module 581 — covers src modules [2321, 2322, 2323, 2324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2321 import add_2321
from module_2322 import subtract_2322
from module_2323 import multiply_2323
from module_2324 import divide_2324

def test_add_2321():
    assert add_2321(2, 3) == 5

def test_subtract_2322():
    assert subtract_2322(10, 4) == 6

def test_multiply_2323():
    assert multiply_2323(3, 7) == 21

def test_divide_2324():
    assert divide_2324(10, 2) == 5.0
