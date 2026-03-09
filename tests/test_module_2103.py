"""Tests for test module 2103 — covers src modules [8409, 8410, 8411, 8412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8409 import add_8409
from module_8410 import subtract_8410
from module_8411 import multiply_8411
from module_8412 import divide_8412

def test_add_8409():
    assert add_8409(2, 3) == 5

def test_subtract_8410():
    assert subtract_8410(10, 4) == 6

def test_multiply_8411():
    assert multiply_8411(3, 7) == 21

def test_divide_8412():
    assert divide_8412(10, 2) == 5.0
