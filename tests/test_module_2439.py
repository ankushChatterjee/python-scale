"""Tests for test module 2439 — covers src modules [9753, 9754, 9755, 9756]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9753 import add_9753
from module_9754 import subtract_9754
from module_9755 import multiply_9755
from module_9756 import divide_9756

def test_add_9753():
    assert add_9753(2, 3) == 5

def test_subtract_9754():
    assert subtract_9754(10, 4) == 6

def test_multiply_9755():
    assert multiply_9755(3, 7) == 21

def test_divide_9756():
    assert divide_9756(10, 2) == 5.0
