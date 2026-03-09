"""Tests for test module 433 — covers src modules [1729, 1730, 1731, 1732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1729 import add_1729
from module_1730 import subtract_1730
from module_1731 import multiply_1731
from module_1732 import divide_1732

def test_add_1729():
    assert add_1729(2, 3) == 5

def test_subtract_1730():
    assert subtract_1730(10, 4) == 6

def test_multiply_1731():
    assert multiply_1731(3, 7) == 21

def test_divide_1732():
    assert divide_1732(10, 2) == 5.0
