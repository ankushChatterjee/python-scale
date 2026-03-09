"""Tests for test module 989 — covers src modules [3953, 3954, 3955, 3956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3953 import add_3953
from module_3954 import subtract_3954
from module_3955 import multiply_3955
from module_3956 import divide_3956

def test_add_3953():
    assert add_3953(2, 3) == 5

def test_subtract_3954():
    assert subtract_3954(10, 4) == 6

def test_multiply_3955():
    assert multiply_3955(3, 7) == 21

def test_divide_3956():
    assert divide_3956(10, 2) == 5.0
