"""Tests for test module 1711 — covers src modules [6841, 6842, 6843, 6844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6841 import add_6841
from module_6842 import subtract_6842
from module_6843 import multiply_6843
from module_6844 import divide_6844

def test_add_6841():
    assert add_6841(2, 3) == 5

def test_subtract_6842():
    assert subtract_6842(10, 4) == 6

def test_multiply_6843():
    assert multiply_6843(3, 7) == 21

def test_divide_6844():
    assert divide_6844(10, 2) == 5.0
