"""Tests for test module 1361 — covers src modules [5441, 5442, 5443, 5444]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5441 import add_5441
from module_5442 import subtract_5442
from module_5443 import multiply_5443
from module_5444 import divide_5444

def test_add_5441():
    assert add_5441(2, 3) == 5

def test_subtract_5442():
    assert subtract_5442(10, 4) == 6

def test_multiply_5443():
    assert multiply_5443(3, 7) == 21

def test_divide_5444():
    assert divide_5444(10, 2) == 5.0
