"""Tests for test module 1921 — covers src modules [7681, 7682, 7683, 7684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7681 import add_7681
from module_7682 import subtract_7682
from module_7683 import multiply_7683
from module_7684 import divide_7684

def test_add_7681():
    assert add_7681(2, 3) == 5

def test_subtract_7682():
    assert subtract_7682(10, 4) == 6

def test_multiply_7683():
    assert multiply_7683(3, 7) == 21

def test_divide_7684():
    assert divide_7684(10, 2) == 5.0
