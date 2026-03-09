"""Tests for test module 439 — covers src modules [1753, 1754, 1755, 1756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1753 import add_1753
from module_1754 import subtract_1754
from module_1755 import multiply_1755
from module_1756 import divide_1756

def test_add_1753():
    assert add_1753(2, 3) == 5

def test_subtract_1754():
    assert subtract_1754(10, 4) == 6

def test_multiply_1755():
    assert multiply_1755(3, 7) == 21

def test_divide_1756():
    assert divide_1756(10, 2) == 5.0
