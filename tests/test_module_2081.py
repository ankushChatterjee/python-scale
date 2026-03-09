"""Tests for test module 2081 — covers src modules [8321, 8322, 8323, 8324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8321 import add_8321
from module_8322 import subtract_8322
from module_8323 import multiply_8323
from module_8324 import divide_8324

def test_add_8321():
    assert add_8321(2, 3) == 5

def test_subtract_8322():
    assert subtract_8322(10, 4) == 6

def test_multiply_8323():
    assert multiply_8323(3, 7) == 21

def test_divide_8324():
    assert divide_8324(10, 2) == 5.0
