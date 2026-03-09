"""Tests for test module 1695 — covers src modules [6777, 6778, 6779, 6780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6777 import add_6777
from module_6778 import subtract_6778
from module_6779 import multiply_6779
from module_6780 import divide_6780

def test_add_6777():
    assert add_6777(2, 3) == 5

def test_subtract_6778():
    assert subtract_6778(10, 4) == 6

def test_multiply_6779():
    assert multiply_6779(3, 7) == 21

def test_divide_6780():
    assert divide_6780(10, 2) == 5.0
