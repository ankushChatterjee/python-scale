"""Tests for test module 1421 — covers src modules [5681, 5682, 5683, 5684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5681 import add_5681
from module_5682 import subtract_5682
from module_5683 import multiply_5683
from module_5684 import divide_5684

def test_add_5681():
    assert add_5681(2, 3) == 5

def test_subtract_5682():
    assert subtract_5682(10, 4) == 6

def test_multiply_5683():
    assert multiply_5683(3, 7) == 21

def test_divide_5684():
    assert divide_5684(10, 2) == 5.0
