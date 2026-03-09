"""Tests for test module 1933 — covers src modules [7729, 7730, 7731, 7732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7729 import add_7729
from module_7730 import subtract_7730
from module_7731 import multiply_7731
from module_7732 import divide_7732

def test_add_7729():
    assert add_7729(2, 3) == 5

def test_subtract_7730():
    assert subtract_7730(10, 4) == 6

def test_multiply_7731():
    assert multiply_7731(3, 7) == 21

def test_divide_7732():
    assert divide_7732(10, 2) == 5.0
