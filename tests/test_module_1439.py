"""Tests for test module 1439 — covers src modules [5753, 5754, 5755, 5756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5753 import add_5753
from module_5754 import subtract_5754
from module_5755 import multiply_5755
from module_5756 import divide_5756

def test_add_5753():
    assert add_5753(2, 3) == 5

def test_subtract_5754():
    assert subtract_5754(10, 4) == 6

def test_multiply_5755():
    assert multiply_5755(3, 7) == 21

def test_divide_5756():
    assert divide_5756(10, 2) == 5.0
