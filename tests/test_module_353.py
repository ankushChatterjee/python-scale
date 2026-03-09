"""Tests for test module 353 — covers src modules [1409, 1410, 1411, 1412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1409 import add_1409
from module_1410 import subtract_1410
from module_1411 import multiply_1411
from module_1412 import divide_1412

def test_add_1409():
    assert add_1409(2, 3) == 5

def test_subtract_1410():
    assert subtract_1410(10, 4) == 6

def test_multiply_1411():
    assert multiply_1411(3, 7) == 21

def test_divide_1412():
    assert divide_1412(10, 2) == 5.0
