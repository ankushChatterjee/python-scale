"""Tests for test module 2445 — covers src modules [9777, 9778, 9779, 9780]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9777 import add_9777
from module_9778 import subtract_9778
from module_9779 import multiply_9779
from module_9780 import divide_9780

def test_add_9777():
    assert add_9777(2, 3) == 5

def test_subtract_9778():
    assert subtract_9778(10, 4) == 6

def test_multiply_9779():
    assert multiply_9779(3, 7) == 21

def test_divide_9780():
    assert divide_9780(10, 2) == 5.0
