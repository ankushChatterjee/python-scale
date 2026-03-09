"""Tests for test module 1081 — covers src modules [4321, 4322, 4323, 4324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4321 import add_4321
from module_4322 import subtract_4322
from module_4323 import multiply_4323
from module_4324 import divide_4324

def test_add_4321():
    assert add_4321(2, 3) == 5

def test_subtract_4322():
    assert subtract_4322(10, 4) == 6

def test_multiply_4323():
    assert multiply_4323(3, 7) == 21

def test_divide_4324():
    assert divide_4324(10, 2) == 5.0
