"""Tests for test module 2177 — covers src modules [8705, 8706, 8707, 8708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8705 import add_8705
from module_8706 import subtract_8706
from module_8707 import multiply_8707
from module_8708 import divide_8708

def test_add_8705():
    assert add_8705(2, 3) == 5

def test_subtract_8706():
    assert subtract_8706(10, 4) == 6

def test_multiply_8707():
    assert multiply_8707(3, 7) == 21

def test_divide_8708():
    assert divide_8708(10, 2) == 5.0
