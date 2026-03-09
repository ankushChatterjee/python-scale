"""Tests for test module 2195 — covers src modules [8777, 8778, 8779, 8780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8777 import add_8777
from module_8778 import subtract_8778
from module_8779 import multiply_8779
from module_8780 import divide_8780

def test_add_8777():
    assert add_8777(2, 3) == 5

def test_subtract_8778():
    assert subtract_8778(10, 4) == 6

def test_multiply_8779():
    assert multiply_8779(3, 7) == 21

def test_divide_8780():
    assert divide_8780(10, 2) == 5.0
