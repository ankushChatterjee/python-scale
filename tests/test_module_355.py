"""Tests for test module 355 — covers src modules [1417, 1418, 1419, 1420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1417 import add_1417
from module_1418 import subtract_1418
from module_1419 import multiply_1419
from module_1420 import divide_1420

def test_add_1417():
    assert add_1417(2, 3) == 5

def test_subtract_1418():
    assert subtract_1418(10, 4) == 6

def test_multiply_1419():
    assert multiply_1419(3, 7) == 21

def test_divide_1420():
    assert divide_1420(10, 2) == 5.0
