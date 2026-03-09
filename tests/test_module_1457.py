"""Tests for test module 1457 — covers src modules [5825, 5826, 5827, 5828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5825 import add_5825
from module_5826 import subtract_5826
from module_5827 import multiply_5827
from module_5828 import divide_5828

def test_add_5825():
    assert add_5825(2, 3) == 5

def test_subtract_5826():
    assert subtract_5826(10, 4) == 6

def test_multiply_5827():
    assert multiply_5827(3, 7) == 21

def test_divide_5828():
    assert divide_5828(10, 2) == 5.0
