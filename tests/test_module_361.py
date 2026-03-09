"""Tests for test module 361 — covers src modules [1441, 1442, 1443, 1444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1441 import add_1441
from module_1442 import subtract_1442
from module_1443 import multiply_1443
from module_1444 import divide_1444

def test_add_1441():
    assert add_1441(2, 3) == 5

def test_subtract_1442():
    assert subtract_1442(10, 4) == 6

def test_multiply_1443():
    assert multiply_1443(3, 7) == 21

def test_divide_1444():
    assert divide_1444(10, 2) == 5.0
