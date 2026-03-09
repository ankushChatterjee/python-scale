"""Tests for test module 1575 — covers src modules [6297, 6298, 6299, 6300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6297 import add_6297
from module_6298 import subtract_6298
from module_6299 import multiply_6299
from module_6300 import divide_6300

def test_add_6297():
    assert add_6297(2, 3) == 5

def test_subtract_6298():
    assert subtract_6298(10, 4) == 6

def test_multiply_6299():
    assert multiply_6299(3, 7) == 21

def test_divide_6300():
    assert divide_6300(10, 2) == 5.0
