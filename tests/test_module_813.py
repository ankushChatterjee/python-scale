"""Tests for test module 813 — covers src modules [3249, 3250, 3251, 3252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3249 import add_3249
from module_3250 import subtract_3250
from module_3251 import multiply_3251
from module_3252 import divide_3252

def test_add_3249():
    assert add_3249(2, 3) == 5

def test_subtract_3250():
    assert subtract_3250(10, 4) == 6

def test_multiply_3251():
    assert multiply_3251(3, 7) == 21

def test_divide_3252():
    assert divide_3252(10, 2) == 5.0
