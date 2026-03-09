"""Tests for test module 75 — covers src modules [297, 298, 299, 300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_297 import add_297
from module_298 import subtract_298
from module_299 import multiply_299
from module_300 import divide_300

def test_add_297():
    assert add_297(2, 3) == 5

def test_subtract_298():
    assert subtract_298(10, 4) == 6

def test_multiply_299():
    assert multiply_299(3, 7) == 21

def test_divide_300():
    assert divide_300(10, 2) == 5.0
