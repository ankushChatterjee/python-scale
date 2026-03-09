"""Tests for test module 1939 — covers src modules [7753, 7754, 7755, 7756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7753 import add_7753
from module_7754 import subtract_7754
from module_7755 import multiply_7755
from module_7756 import divide_7756

def test_add_7753():
    assert add_7753(2, 3) == 5

def test_subtract_7754():
    assert subtract_7754(10, 4) == 6

def test_multiply_7755():
    assert multiply_7755(3, 7) == 21

def test_divide_7756():
    assert divide_7756(10, 2) == 5.0
