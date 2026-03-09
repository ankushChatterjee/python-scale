"""Tests for test module 2425 — covers src modules [9697, 9698, 9699, 9700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9697 import add_9697
from module_9698 import subtract_9698
from module_9699 import multiply_9699
from module_9700 import divide_9700

def test_add_9697():
    assert add_9697(2, 3) == 5

def test_subtract_9698():
    assert subtract_9698(10, 4) == 6

def test_multiply_9699():
    assert multiply_9699(3, 7) == 21

def test_divide_9700():
    assert divide_9700(10, 2) == 5.0
