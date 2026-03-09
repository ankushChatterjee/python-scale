"""Tests for test module 1557 — covers src modules [6225, 6226, 6227, 6228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6225 import add_6225
from module_6226 import subtract_6226
from module_6227 import multiply_6227
from module_6228 import divide_6228

def test_add_6225():
    assert add_6225(2, 3) == 5

def test_subtract_6226():
    assert subtract_6226(10, 4) == 6

def test_multiply_6227():
    assert multiply_6227(3, 7) == 21

def test_divide_6228():
    assert divide_6228(10, 2) == 5.0
