"""Tests for test module 347 — covers src modules [1385, 1386, 1387, 1388]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1385 import add_1385
from module_1386 import subtract_1386
from module_1387 import multiply_1387
from module_1388 import divide_1388

def test_add_1385():
    assert add_1385(2, 3) == 5

def test_subtract_1386():
    assert subtract_1386(10, 4) == 6

def test_multiply_1387():
    assert multiply_1387(3, 7) == 21

def test_divide_1388():
    assert divide_1388(10, 2) == 5.0
