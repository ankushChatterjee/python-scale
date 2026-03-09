"""Tests for test module 1853 — covers src modules [7409, 7410, 7411, 7412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7409 import add_7409
from module_7410 import subtract_7410
from module_7411 import multiply_7411
from module_7412 import divide_7412

def test_add_7409():
    assert add_7409(2, 3) == 5

def test_subtract_7410():
    assert subtract_7410(10, 4) == 6

def test_multiply_7411():
    assert multiply_7411(3, 7) == 21

def test_divide_7412():
    assert divide_7412(10, 2) == 5.0
