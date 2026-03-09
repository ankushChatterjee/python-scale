"""Tests for test module 123 — covers src modules [489, 490, 491, 492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_489 import add_489
from module_490 import subtract_490
from module_491 import multiply_491
from module_492 import divide_492

def test_add_489():
    assert add_489(2, 3) == 5

def test_subtract_490():
    assert subtract_490(10, 4) == 6

def test_multiply_491():
    assert multiply_491(3, 7) == 21

def test_divide_492():
    assert divide_492(10, 2) == 5.0
