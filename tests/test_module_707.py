"""Tests for test module 707 — covers src modules [2825, 2826, 2827, 2828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2825 import add_2825
from module_2826 import subtract_2826
from module_2827 import multiply_2827
from module_2828 import divide_2828

def test_add_2825():
    assert add_2825(2, 3) == 5

def test_subtract_2826():
    assert subtract_2826(10, 4) == 6

def test_multiply_2827():
    assert multiply_2827(3, 7) == 21

def test_divide_2828():
    assert divide_2828(10, 2) == 5.0
