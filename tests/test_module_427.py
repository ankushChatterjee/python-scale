"""Tests for test module 427 — covers src modules [1705, 1706, 1707, 1708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1705 import add_1705
from module_1706 import subtract_1706
from module_1707 import multiply_1707
from module_1708 import divide_1708

def test_add_1705():
    assert add_1705(2, 3) == 5

def test_subtract_1706():
    assert subtract_1706(10, 4) == 6

def test_multiply_1707():
    assert multiply_1707(3, 7) == 21

def test_divide_1708():
    assert divide_1708(10, 2) == 5.0
