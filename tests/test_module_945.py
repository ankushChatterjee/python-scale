"""Tests for test module 945 — covers src modules [3777, 3778, 3779, 3780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3777 import add_3777
from module_3778 import subtract_3778
from module_3779 import multiply_3779
from module_3780 import divide_3780

def test_add_3777():
    assert add_3777(2, 3) == 5

def test_subtract_3778():
    assert subtract_3778(10, 4) == 6

def test_multiply_3779():
    assert multiply_3779(3, 7) == 21

def test_divide_3780():
    assert divide_3780(10, 2) == 5.0
