"""Tests for test module 1623 — covers src modules [6489, 6490, 6491, 6492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6489 import add_6489
from module_6490 import subtract_6490
from module_6491 import multiply_6491
from module_6492 import divide_6492

def test_add_6489():
    assert add_6489(2, 3) == 5

def test_subtract_6490():
    assert subtract_6490(10, 4) == 6

def test_multiply_6491():
    assert multiply_6491(3, 7) == 21

def test_divide_6492():
    assert divide_6492(10, 2) == 5.0
