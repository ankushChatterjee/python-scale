"""Tests for test module 1913 — covers src modules [7649, 7650, 7651, 7652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7649 import add_7649
from module_7650 import subtract_7650
from module_7651 import multiply_7651
from module_7652 import divide_7652

def test_add_7649():
    assert add_7649(2, 3) == 5

def test_subtract_7650():
    assert subtract_7650(10, 4) == 6

def test_multiply_7651():
    assert multiply_7651(3, 7) == 21

def test_divide_7652():
    assert divide_7652(10, 2) == 5.0
