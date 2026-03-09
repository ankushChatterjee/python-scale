"""Tests for test module 853 — covers src modules [3409, 3410, 3411, 3412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3409 import add_3409
from module_3410 import subtract_3410
from module_3411 import multiply_3411
from module_3412 import divide_3412

def test_add_3409():
    assert add_3409(2, 3) == 5

def test_subtract_3410():
    assert subtract_3410(10, 4) == 6

def test_multiply_3411():
    assert multiply_3411(3, 7) == 21

def test_divide_3412():
    assert divide_3412(10, 2) == 5.0
