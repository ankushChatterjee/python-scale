"""Tests for test module 1103 — covers src modules [4409, 4410, 4411, 4412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4409 import add_4409
from module_4410 import subtract_4410
from module_4411 import multiply_4411
from module_4412 import divide_4412

def test_add_4409():
    assert add_4409(2, 3) == 5

def test_subtract_4410():
    assert subtract_4410(10, 4) == 6

def test_multiply_4411():
    assert multiply_4411(3, 7) == 21

def test_divide_4412():
    assert divide_4412(10, 2) == 5.0
