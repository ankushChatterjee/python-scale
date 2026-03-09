"""Tests for test module 1239 — covers src modules [4953, 4954, 4955, 4956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4953 import add_4953
from module_4954 import subtract_4954
from module_4955 import multiply_4955
from module_4956 import divide_4956

def test_add_4953():
    assert add_4953(2, 3) == 5

def test_subtract_4954():
    assert subtract_4954(10, 4) == 6

def test_multiply_4955():
    assert multiply_4955(3, 7) == 21

def test_divide_4956():
    assert divide_4956(10, 2) == 5.0
