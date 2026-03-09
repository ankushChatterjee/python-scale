"""Tests for test module 695 — covers src modules [2777, 2778, 2779, 2780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2777 import add_2777
from module_2778 import subtract_2778
from module_2779 import multiply_2779
from module_2780 import divide_2780

def test_add_2777():
    assert add_2777(2, 3) == 5

def test_subtract_2778():
    assert subtract_2778(10, 4) == 6

def test_multiply_2779():
    assert multiply_2779(3, 7) == 21

def test_divide_2780():
    assert divide_2780(10, 2) == 5.0
