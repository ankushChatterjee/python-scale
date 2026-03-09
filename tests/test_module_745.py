"""Tests for test module 745 — covers src modules [2977, 2978, 2979, 2980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2977 import add_2977
from module_2978 import subtract_2978
from module_2979 import multiply_2979
from module_2980 import divide_2980

def test_add_2977():
    assert add_2977(2, 3) == 5

def test_subtract_2978():
    assert subtract_2978(10, 4) == 6

def test_multiply_2979():
    assert multiply_2979(3, 7) == 21

def test_divide_2980():
    assert divide_2980(10, 2) == 5.0
