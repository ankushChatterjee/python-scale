"""Tests for test module 81 — covers src modules [321, 322, 323, 324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_321 import add_321
from module_322 import subtract_322
from module_323 import multiply_323
from module_324 import divide_324

def test_add_321():
    assert add_321(2, 3) == 5

def test_subtract_322():
    assert subtract_322(10, 4) == 6

def test_multiply_323():
    assert multiply_323(3, 7) == 21

def test_divide_324():
    assert divide_324(10, 2) == 5.0
