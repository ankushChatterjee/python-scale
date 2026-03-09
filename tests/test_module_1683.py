"""Tests for test module 1683 — covers src modules [6729, 6730, 6731, 6732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6729 import add_6729
from module_6730 import subtract_6730
from module_6731 import multiply_6731
from module_6732 import divide_6732

def test_add_6729():
    assert add_6729(2, 3) == 5

def test_subtract_6730():
    assert subtract_6730(10, 4) == 6

def test_multiply_6731():
    assert multiply_6731(3, 7) == 21

def test_divide_6732():
    assert divide_6732(10, 2) == 5.0
