"""Tests for test module 2325 — covers src modules [9297, 9298, 9299, 9300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9297 import add_9297
from module_9298 import subtract_9298
from module_9299 import multiply_9299
from module_9300 import divide_9300

def test_add_9297():
    assert add_9297(2, 3) == 5

def test_subtract_9298():
    assert subtract_9298(10, 4) == 6

def test_multiply_9299():
    assert multiply_9299(3, 7) == 21

def test_divide_9300():
    assert divide_9300(10, 2) == 5.0
