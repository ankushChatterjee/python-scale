"""Tests for test module 1353 — covers src modules [5409, 5410, 5411, 5412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5409 import add_5409
from module_5410 import subtract_5410
from module_5411 import multiply_5411
from module_5412 import divide_5412

def test_add_5409():
    assert add_5409(2, 3) == 5

def test_subtract_5410():
    assert subtract_5410(10, 4) == 6

def test_multiply_5411():
    assert multiply_5411(3, 7) == 21

def test_divide_5412():
    assert divide_5412(10, 2) == 5.0
