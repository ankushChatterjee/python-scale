"""Tests for test module 1611 — covers src modules [6441, 6442, 6443, 6444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6441 import add_6441
from module_6442 import subtract_6442
from module_6443 import multiply_6443
from module_6444 import divide_6444

def test_add_6441():
    assert add_6441(2, 3) == 5

def test_subtract_6442():
    assert subtract_6442(10, 4) == 6

def test_multiply_6443():
    assert multiply_6443(3, 7) == 21

def test_divide_6444():
    assert divide_6444(10, 2) == 5.0
