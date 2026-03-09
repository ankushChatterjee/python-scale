"""Tests for test module 197 — covers src modules [785, 786, 787, 788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_785 import add_785
from module_786 import subtract_786
from module_787 import multiply_787
from module_788 import divide_788

def test_add_785():
    assert add_785(2, 3) == 5

def test_subtract_786():
    assert subtract_786(10, 4) == 6

def test_multiply_787():
    assert multiply_787(3, 7) == 21

def test_divide_788():
    assert divide_788(10, 2) == 5.0
