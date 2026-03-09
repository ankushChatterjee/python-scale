"""Tests for test module 611 — covers src modules [2441, 2442, 2443, 2444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2441 import add_2441
from module_2442 import subtract_2442
from module_2443 import multiply_2443
from module_2444 import divide_2444

def test_add_2441():
    assert add_2441(2, 3) == 5

def test_subtract_2442():
    assert subtract_2442(10, 4) == 6

def test_multiply_2443():
    assert multiply_2443(3, 7) == 21

def test_divide_2444():
    assert divide_2444(10, 2) == 5.0
