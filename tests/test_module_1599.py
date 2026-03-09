"""Tests for test module 1599 — covers src modules [6393, 6394, 6395, 6396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6393 import add_6393
from module_6394 import subtract_6394
from module_6395 import multiply_6395
from module_6396 import divide_6396

def test_add_6393():
    assert add_6393(2, 3) == 5

def test_subtract_6394():
    assert subtract_6394(10, 4) == 6

def test_multiply_6395():
    assert multiply_6395(3, 7) == 21

def test_divide_6396():
    assert divide_6396(10, 2) == 5.0
