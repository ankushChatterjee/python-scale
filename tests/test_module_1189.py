"""Tests for test module 1189 — covers src modules [4753, 4754, 4755, 4756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4753 import add_4753
from module_4754 import subtract_4754
from module_4755 import multiply_4755
from module_4756 import divide_4756

def test_add_4753():
    assert add_4753(2, 3) == 5

def test_subtract_4754():
    assert subtract_4754(10, 4) == 6

def test_multiply_4755():
    assert multiply_4755(3, 7) == 21

def test_divide_4756():
    assert divide_4756(10, 2) == 5.0
