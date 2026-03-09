"""Tests for test module 1989 — covers src modules [7953, 7954, 7955, 7956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7953 import add_7953
from module_7954 import subtract_7954
from module_7955 import multiply_7955
from module_7956 import divide_7956

def test_add_7953():
    assert add_7953(2, 3) == 5

def test_subtract_7954():
    assert subtract_7954(10, 4) == 6

def test_multiply_7955():
    assert multiply_7955(3, 7) == 21

def test_divide_7956():
    assert divide_7956(10, 2) == 5.0
