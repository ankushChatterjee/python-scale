"""Tests for test module 1195 — covers src modules [4777, 4778, 4779, 4780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4777 import add_4777
from module_4778 import subtract_4778
from module_4779 import multiply_4779
from module_4780 import divide_4780

def test_add_4777():
    assert add_4777(2, 3) == 5

def test_subtract_4778():
    assert subtract_4778(10, 4) == 6

def test_multiply_4779():
    assert multiply_4779(3, 7) == 21

def test_divide_4780():
    assert divide_4780(10, 2) == 5.0
