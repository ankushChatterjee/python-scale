"""Tests for test module 939 — covers src modules [3753, 3754, 3755, 3756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3753 import add_3753
from module_3754 import subtract_3754
from module_3755 import multiply_3755
from module_3756 import divide_3756

def test_add_3753():
    assert add_3753(2, 3) == 5

def test_subtract_3754():
    assert subtract_3754(10, 4) == 6

def test_multiply_3755():
    assert multiply_3755(3, 7) == 21

def test_divide_3756():
    assert divide_3756(10, 2) == 5.0
