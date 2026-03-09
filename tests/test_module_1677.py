"""Tests for test module 1677 — covers src modules [6705, 6706, 6707, 6708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6705 import add_6705
from module_6706 import subtract_6706
from module_6707 import multiply_6707
from module_6708 import divide_6708

def test_add_6705():
    assert add_6705(2, 3) == 5

def test_subtract_6706():
    assert subtract_6706(10, 4) == 6

def test_multiply_6707():
    assert multiply_6707(3, 7) == 21

def test_divide_6708():
    assert divide_6708(10, 2) == 5.0
