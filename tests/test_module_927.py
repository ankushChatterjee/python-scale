"""Tests for test module 927 — covers src modules [3705, 3706, 3707, 3708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3705 import add_3705
from module_3706 import subtract_3706
from module_3707 import multiply_3707
from module_3708 import divide_3708

def test_add_3705():
    assert add_3705(2, 3) == 5

def test_subtract_3706():
    assert subtract_3706(10, 4) == 6

def test_multiply_3707():
    assert multiply_3707(3, 7) == 21

def test_divide_3708():
    assert divide_3708(10, 2) == 5.0
