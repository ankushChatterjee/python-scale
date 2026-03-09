"""Tests for test module 395 — covers src modules [1577, 1578, 1579, 1580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1577 import add_1577
from module_1578 import subtract_1578
from module_1579 import multiply_1579
from module_1580 import divide_1580

def test_add_1577():
    assert add_1577(2, 3) == 5

def test_subtract_1578():
    assert subtract_1578(10, 4) == 6

def test_multiply_1579():
    assert multiply_1579(3, 7) == 21

def test_divide_1580():
    assert divide_1580(10, 2) == 5.0
