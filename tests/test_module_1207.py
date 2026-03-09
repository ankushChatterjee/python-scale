"""Tests for test module 1207 — covers src modules [4825, 4826, 4827, 4828]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4825 import add_4825
from module_4826 import subtract_4826
from module_4827 import multiply_4827
from module_4828 import divide_4828

def test_add_4825():
    assert add_4825(2, 3) == 5

def test_subtract_4826():
    assert subtract_4826(10, 4) == 6

def test_multiply_4827():
    assert multiply_4827(3, 7) == 21

def test_divide_4828():
    assert divide_4828(10, 2) == 5.0
