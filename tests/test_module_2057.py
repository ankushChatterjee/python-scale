"""Tests for test module 2057 — covers src modules [8225, 8226, 8227, 8228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8225 import add_8225
from module_8226 import subtract_8226
from module_8227 import multiply_8227
from module_8228 import divide_8228

def test_add_8225():
    assert add_8225(2, 3) == 5

def test_subtract_8226():
    assert subtract_8226(10, 4) == 6

def test_multiply_8227():
    assert multiply_8227(3, 7) == 21

def test_divide_8228():
    assert divide_8228(10, 2) == 5.0
