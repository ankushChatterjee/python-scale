"""Tests for test module 1831 — covers src modules [7321, 7322, 7323, 7324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7321 import add_7321
from module_7322 import subtract_7322
from module_7323 import multiply_7323
from module_7324 import divide_7324

def test_add_7321():
    assert add_7321(2, 3) == 5

def test_subtract_7322():
    assert subtract_7322(10, 4) == 6

def test_multiply_7323():
    assert multiply_7323(3, 7) == 21

def test_divide_7324():
    assert divide_7324(10, 2) == 5.0
