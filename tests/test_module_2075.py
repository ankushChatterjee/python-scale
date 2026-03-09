"""Tests for test module 2075 — covers src modules [8297, 8298, 8299, 8300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8297 import add_8297
from module_8298 import subtract_8298
from module_8299 import multiply_8299
from module_8300 import divide_8300

def test_add_8297():
    assert add_8297(2, 3) == 5

def test_subtract_8298():
    assert subtract_8298(10, 4) == 6

def test_multiply_8299():
    assert multiply_8299(3, 7) == 21

def test_divide_8300():
    assert divide_8300(10, 2) == 5.0
