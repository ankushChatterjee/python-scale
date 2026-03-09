"""Tests for test module 1063 — covers src modules [4249, 4250, 4251, 4252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4249 import add_4249
from module_4250 import subtract_4250
from module_4251 import multiply_4251
from module_4252 import divide_4252

def test_add_4249():
    assert add_4249(2, 3) == 5

def test_subtract_4250():
    assert subtract_4250(10, 4) == 6

def test_multiply_4251():
    assert multiply_4251(3, 7) == 21

def test_divide_4252():
    assert divide_4252(10, 2) == 5.0
