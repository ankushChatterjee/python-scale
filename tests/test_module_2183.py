"""Tests for test module 2183 — covers src modules [8729, 8730, 8731, 8732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8729 import add_8729
from module_8730 import subtract_8730
from module_8731 import multiply_8731
from module_8732 import divide_8732

def test_add_8729():
    assert add_8729(2, 3) == 5

def test_subtract_8730():
    assert subtract_8730(10, 4) == 6

def test_multiply_8731():
    assert multiply_8731(3, 7) == 21

def test_divide_8732():
    assert divide_8732(10, 2) == 5.0
