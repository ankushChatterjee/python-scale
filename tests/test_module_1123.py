"""Tests for test module 1123 — covers src modules [4489, 4490, 4491, 4492]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4489 import add_4489
from module_4490 import subtract_4490
from module_4491 import multiply_4491
from module_4492 import divide_4492

def test_add_4489():
    assert add_4489(2, 3) == 5

def test_subtract_4490():
    assert subtract_4490(10, 4) == 6

def test_multiply_4491():
    assert multiply_4491(3, 7) == 21

def test_divide_4492():
    assert divide_4492(10, 2) == 5.0
