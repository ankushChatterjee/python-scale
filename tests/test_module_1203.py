"""Tests for test module 1203 — covers src modules [4809, 4810, 4811, 4812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4809 import add_4809
from module_4810 import subtract_4810
from module_4811 import multiply_4811
from module_4812 import divide_4812

def test_add_4809():
    assert add_4809(2, 3) == 5

def test_subtract_4810():
    assert subtract_4810(10, 4) == 6

def test_multiply_4811():
    assert multiply_4811(3, 7) == 21

def test_divide_4812():
    assert divide_4812(10, 2) == 5.0
