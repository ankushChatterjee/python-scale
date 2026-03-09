"""Tests for test module 2207 — covers src modules [8825, 8826, 8827, 8828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8825 import add_8825
from module_8826 import subtract_8826
from module_8827 import multiply_8827
from module_8828 import divide_8828

def test_add_8825():
    assert add_8825(2, 3) == 5

def test_subtract_8826():
    assert subtract_8826(10, 4) == 6

def test_multiply_8827():
    assert multiply_8827(3, 7) == 21

def test_divide_8828():
    assert divide_8828(10, 2) == 5.0
