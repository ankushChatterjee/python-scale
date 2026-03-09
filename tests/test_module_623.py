"""Tests for test module 623 — covers src modules [2489, 2490, 2491, 2492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2489 import add_2489
from module_2490 import subtract_2490
from module_2491 import multiply_2491
from module_2492 import divide_2492

def test_add_2489():
    assert add_2489(2, 3) == 5

def test_subtract_2490():
    assert subtract_2490(10, 4) == 6

def test_multiply_2491():
    assert multiply_2491(3, 7) == 21

def test_divide_2492():
    assert divide_2492(10, 2) == 5.0
