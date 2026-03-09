"""Tests for test module 1111 — covers src modules [4441, 4442, 4443, 4444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4441 import add_4441
from module_4442 import subtract_4442
from module_4443 import multiply_4443
from module_4444 import divide_4444

def test_add_4441():
    assert add_4441(2, 3) == 5

def test_subtract_4442():
    assert subtract_4442(10, 4) == 6

def test_multiply_4443():
    assert multiply_4443(3, 7) == 21

def test_divide_4444():
    assert divide_4444(10, 2) == 5.0
