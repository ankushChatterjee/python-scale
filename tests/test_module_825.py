"""Tests for test module 825 — covers src modules [3297, 3298, 3299, 3300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3297 import add_3297
from module_3298 import subtract_3298
from module_3299 import multiply_3299
from module_3300 import divide_3300

def test_add_3297():
    assert add_3297(2, 3) == 5

def test_subtract_3298():
    assert subtract_3298(10, 4) == 6

def test_multiply_3299():
    assert multiply_3299(3, 7) == 21

def test_divide_3300():
    assert divide_3300(10, 2) == 5.0
