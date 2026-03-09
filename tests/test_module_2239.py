"""Tests for test module 2239 — covers src modules [8953, 8954, 8955, 8956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8953 import add_8953
from module_8954 import subtract_8954
from module_8955 import multiply_8955
from module_8956 import divide_8956

def test_add_8953():
    assert add_8953(2, 3) == 5

def test_subtract_8954():
    assert subtract_8954(10, 4) == 6

def test_multiply_8955():
    assert multiply_8955(3, 7) == 21

def test_divide_8956():
    assert divide_8956(10, 2) == 5.0
