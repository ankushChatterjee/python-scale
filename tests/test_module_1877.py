"""Tests for test module 1877 — covers src modules [7505, 7506, 7507, 7508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7505 import add_7505
from module_7506 import subtract_7506
from module_7507 import multiply_7507
from module_7508 import divide_7508

def test_add_7505():
    assert add_7505(2, 3) == 5

def test_subtract_7506():
    assert subtract_7506(10, 4) == 6

def test_multiply_7507():
    assert multiply_7507(3, 7) == 21

def test_divide_7508():
    assert divide_7508(10, 2) == 5.0
