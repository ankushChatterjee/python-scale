"""Tests for test module 1689 — covers src modules [6753, 6754, 6755, 6756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6753 import add_6753
from module_6754 import subtract_6754
from module_6755 import multiply_6755
from module_6756 import divide_6756

def test_add_6753():
    assert add_6753(2, 3) == 5

def test_subtract_6754():
    assert subtract_6754(10, 4) == 6

def test_multiply_6755():
    assert multiply_6755(3, 7) == 21

def test_divide_6756():
    assert divide_6756(10, 2) == 5.0
