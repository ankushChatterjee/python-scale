"""Tests for test module 1861 — covers src modules [7441, 7442, 7443, 7444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7441 import add_7441
from module_7442 import subtract_7442
from module_7443 import multiply_7443
from module_7444 import divide_7444

def test_add_7441():
    assert add_7441(2, 3) == 5

def test_subtract_7442():
    assert subtract_7442(10, 4) == 6

def test_multiply_7443():
    assert multiply_7443(3, 7) == 21

def test_divide_7444():
    assert divide_7444(10, 2) == 5.0
