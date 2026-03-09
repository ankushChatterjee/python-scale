"""Tests for test module 103 — covers src modules [409, 410, 411, 412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_409 import add_409
from module_410 import subtract_410
from module_411 import multiply_411
from module_412 import divide_412

def test_add_409():
    assert add_409(2, 3) == 5

def test_subtract_410():
    assert subtract_410(10, 4) == 6

def test_multiply_411():
    assert multiply_411(3, 7) == 21

def test_divide_412():
    assert divide_412(10, 2) == 5.0
