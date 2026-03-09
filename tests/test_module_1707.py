"""Tests for test module 1707 — covers src modules [6825, 6826, 6827, 6828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6825 import add_6825
from module_6826 import subtract_6826
from module_6827 import multiply_6827
from module_6828 import divide_6828

def test_add_6825():
    assert add_6825(2, 3) == 5

def test_subtract_6826():
    assert subtract_6826(10, 4) == 6

def test_multiply_6827():
    assert multiply_6827(3, 7) == 21

def test_divide_6828():
    assert divide_6828(10, 2) == 5.0
