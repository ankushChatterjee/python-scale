"""Tests for test module 375 — covers src modules [1497, 1498, 1499, 1500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1497 import add_1497
from module_1498 import subtract_1498
from module_1499 import multiply_1499
from module_1500 import divide_1500

def test_add_1497():
    assert add_1497(2, 3) == 5

def test_subtract_1498():
    assert subtract_1498(10, 4) == 6

def test_multiply_1499():
    assert multiply_1499(3, 7) == 21

def test_divide_1500():
    assert divide_1500(10, 2) == 5.0
