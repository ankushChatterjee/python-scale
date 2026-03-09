"""Tests for test module 563 — covers src modules [2249, 2250, 2251, 2252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2249 import add_2249
from module_2250 import subtract_2250
from module_2251 import multiply_2251
from module_2252 import divide_2252

def test_add_2249():
    assert add_2249(2, 3) == 5

def test_subtract_2250():
    assert subtract_2250(10, 4) == 6

def test_multiply_2251():
    assert multiply_2251(3, 7) == 21

def test_divide_2252():
    assert divide_2252(10, 2) == 5.0
