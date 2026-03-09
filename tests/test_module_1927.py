"""Tests for test module 1927 — covers src modules [7705, 7706, 7707, 7708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7705 import add_7705
from module_7706 import subtract_7706
from module_7707 import multiply_7707
from module_7708 import divide_7708

def test_add_7705():
    assert add_7705(2, 3) == 5

def test_subtract_7706():
    assert subtract_7706(10, 4) == 6

def test_multiply_7707():
    assert multiply_7707(3, 7) == 21

def test_divide_7708():
    assert divide_7708(10, 2) == 5.0
