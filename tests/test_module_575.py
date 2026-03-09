"""Tests for test module 575 — covers src modules [2297, 2298, 2299, 2300]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2297 import add_2297
from module_2298 import subtract_2298
from module_2299 import multiply_2299
from module_2300 import divide_2300

def test_add_2297():
    assert add_2297(2, 3) == 5

def test_subtract_2298():
    assert subtract_2298(10, 4) == 6

def test_multiply_2299():
    assert multiply_2299(3, 7) == 21

def test_divide_2300():
    assert divide_2300(10, 2) == 5.0
