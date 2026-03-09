"""Tests for test module 195 — covers src modules [777, 778, 779, 780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_777 import add_777
from module_778 import subtract_778
from module_779 import multiply_779
from module_780 import divide_780

def test_add_777():
    assert add_777(2, 3) == 5

def test_subtract_778():
    assert subtract_778(10, 4) == 6

def test_multiply_779():
    assert multiply_779(3, 7) == 21

def test_divide_780():
    assert divide_780(10, 2) == 5.0
