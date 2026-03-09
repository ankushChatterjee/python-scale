"""Tests for test module 1603 — covers src modules [6409, 6410, 6411, 6412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6409 import add_6409
from module_6410 import subtract_6410
from module_6411 import multiply_6411
from module_6412 import divide_6412

def test_add_6409():
    assert add_6409(2, 3) == 5

def test_subtract_6410():
    assert subtract_6410(10, 4) == 6

def test_multiply_6411():
    assert multiply_6411(3, 7) == 21

def test_divide_6412():
    assert divide_6412(10, 2) == 5.0
