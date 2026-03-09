"""Tests for test module 2189 — covers src modules [8753, 8754, 8755, 8756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8753 import add_8753
from module_8754 import subtract_8754
from module_8755 import multiply_8755
from module_8756 import divide_8756

def test_add_8753():
    assert add_8753(2, 3) == 5

def test_subtract_8754():
    assert subtract_8754(10, 4) == 6

def test_multiply_8755():
    assert multiply_8755(3, 7) == 21

def test_divide_8756():
    assert divide_8756(10, 2) == 5.0
