"""Tests for test module 1489 — covers src modules [5953, 5954, 5955, 5956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5953 import add_5953
from module_5954 import subtract_5954
from module_5955 import multiply_5955
from module_5956 import divide_5956

def test_add_5953():
    assert add_5953(2, 3) == 5

def test_subtract_5954():
    assert subtract_5954(10, 4) == 6

def test_multiply_5955():
    assert multiply_5955(3, 7) == 21

def test_divide_5956():
    assert divide_5956(10, 2) == 5.0
