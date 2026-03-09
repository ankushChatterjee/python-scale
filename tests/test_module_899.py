"""Tests for test module 899 — covers src modules [3593, 3594, 3595, 3596]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3593 import add_3593
from module_3594 import subtract_3594
from module_3595 import multiply_3595
from module_3596 import divide_3596

def test_add_3593():
    assert add_3593(2, 3) == 5

def test_subtract_3594():
    assert subtract_3594(10, 4) == 6

def test_multiply_3595():
    assert multiply_3595(3, 7) == 21

def test_divide_3596():
    assert divide_3596(10, 2) == 5.0
