"""Tests for test module 861 — covers src modules [3441, 3442, 3443, 3444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3441 import add_3441
from module_3442 import subtract_3442
from module_3443 import multiply_3443
from module_3444 import divide_3444

def test_add_3441():
    assert add_3441(2, 3) == 5

def test_subtract_3442():
    assert subtract_3442(10, 4) == 6

def test_multiply_3443():
    assert multiply_3443(3, 7) == 21

def test_divide_3444():
    assert divide_3444(10, 2) == 5.0
