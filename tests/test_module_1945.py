"""Tests for test module 1945 — covers src modules [7777, 7778, 7779, 7780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7777 import add_7777
from module_7778 import subtract_7778
from module_7779 import multiply_7779
from module_7780 import divide_7780

def test_add_7777():
    assert add_7777(2, 3) == 5

def test_subtract_7778():
    assert subtract_7778(10, 4) == 6

def test_multiply_7779():
    assert multiply_7779(3, 7) == 21

def test_divide_7780():
    assert divide_7780(10, 2) == 5.0
