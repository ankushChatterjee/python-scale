"""Tests for test module 325 — covers src modules [1297, 1298, 1299, 1300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1297 import add_1297
from module_1298 import subtract_1298
from module_1299 import multiply_1299
from module_1300 import divide_1300

def test_add_1297():
    assert add_1297(2, 3) == 5

def test_subtract_1298():
    assert subtract_1298(10, 4) == 6

def test_multiply_1299():
    assert multiply_1299(3, 7) == 21

def test_divide_1300():
    assert divide_1300(10, 2) == 5.0
