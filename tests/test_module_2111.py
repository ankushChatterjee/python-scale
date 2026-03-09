"""Tests for test module 2111 — covers src modules [8441, 8442, 8443, 8444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8441 import add_8441
from module_8442 import subtract_8442
from module_8443 import multiply_8443
from module_8444 import divide_8444

def test_add_8441():
    assert add_8441(2, 3) == 5

def test_subtract_8442():
    assert subtract_8442(10, 4) == 6

def test_multiply_8443():
    assert multiply_8443(3, 7) == 21

def test_divide_8444():
    assert divide_8444(10, 2) == 5.0
