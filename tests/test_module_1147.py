"""Tests for test module 1147 — covers src modules [4585, 4586, 4587, 4588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4585 import add_4585
from module_4586 import subtract_4586
from module_4587 import multiply_4587
from module_4588 import divide_4588

def test_add_4585():
    assert add_4585(2, 3) == 5

def test_subtract_4586():
    assert subtract_4586(10, 4) == 6

def test_multiply_4587():
    assert multiply_4587(3, 7) == 21

def test_divide_4588():
    assert divide_4588(10, 2) == 5.0
