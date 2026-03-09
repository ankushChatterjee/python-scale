"""Tests for test module 1513 — covers src modules [6049, 6050, 6051, 6052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6049 import add_6049
from module_6050 import subtract_6050
from module_6051 import multiply_6051
from module_6052 import divide_6052

def test_add_6049():
    assert add_6049(2, 3) == 5

def test_subtract_6050():
    assert subtract_6050(10, 4) == 6

def test_multiply_6051():
    assert multiply_6051(3, 7) == 21

def test_divide_6052():
    assert divide_6052(10, 2) == 5.0
