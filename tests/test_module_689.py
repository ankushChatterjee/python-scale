"""Tests for test module 689 — covers src modules [2753, 2754, 2755, 2756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2753 import add_2753
from module_2754 import subtract_2754
from module_2755 import multiply_2755
from module_2756 import divide_2756

def test_add_2753():
    assert add_2753(2, 3) == 5

def test_subtract_2754():
    assert subtract_2754(10, 4) == 6

def test_multiply_2755():
    assert multiply_2755(3, 7) == 21

def test_divide_2756():
    assert divide_2756(10, 2) == 5.0
