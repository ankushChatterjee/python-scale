"""Tests for test module 111 — covers src modules [441, 442, 443, 444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_441 import add_441
from module_442 import subtract_442
from module_443 import multiply_443
from module_444 import divide_444

def test_add_441():
    assert add_441(2, 3) == 5

def test_subtract_442():
    assert subtract_442(10, 4) == 6

def test_multiply_443():
    assert multiply_443(3, 7) == 21

def test_divide_444():
    assert divide_444(10, 2) == 5.0
