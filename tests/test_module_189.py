"""Tests for test module 189 — covers src modules [753, 754, 755, 756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_753 import add_753
from module_754 import subtract_754
from module_755 import multiply_755
from module_756 import divide_756

def test_add_753():
    assert add_753(2, 3) == 5

def test_subtract_754():
    assert subtract_754(10, 4) == 6

def test_multiply_755():
    assert multiply_755(3, 7) == 21

def test_divide_756():
    assert divide_756(10, 2) == 5.0
