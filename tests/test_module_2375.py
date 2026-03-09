"""Tests for test module 2375 — covers src modules [9497, 9498, 9499, 9500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9497 import add_9497
from module_9498 import subtract_9498
from module_9499 import multiply_9499
from module_9500 import divide_9500

def test_add_9497():
    assert add_9497(2, 3) == 5

def test_subtract_9498():
    assert subtract_9498(10, 4) == 6

def test_multiply_9499():
    assert multiply_9499(3, 7) == 21

def test_divide_9500():
    assert divide_9500(10, 2) == 5.0
