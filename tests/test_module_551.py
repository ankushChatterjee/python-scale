"""Tests for test module 551 — covers src modules [2201, 2202, 2203, 2204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2201 import add_2201
from module_2202 import subtract_2202
from module_2203 import multiply_2203
from module_2204 import divide_2204

def test_add_2201():
    assert add_2201(2, 3) == 5

def test_subtract_2202():
    assert subtract_2202(10, 4) == 6

def test_multiply_2203():
    assert multiply_2203(3, 7) == 21

def test_divide_2204():
    assert divide_2204(10, 2) == 5.0
