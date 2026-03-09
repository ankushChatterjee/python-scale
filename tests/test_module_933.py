"""Tests for test module 933 — covers src modules [3729, 3730, 3731, 3732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3729 import add_3729
from module_3730 import subtract_3730
from module_3731 import multiply_3731
from module_3732 import divide_3732

def test_add_3729():
    assert add_3729(2, 3) == 5

def test_subtract_3730():
    assert subtract_3730(10, 4) == 6

def test_multiply_3731():
    assert multiply_3731(3, 7) == 21

def test_divide_3732():
    assert divide_3732(10, 2) == 5.0
