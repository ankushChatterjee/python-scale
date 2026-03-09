"""Tests for test module 1953 — covers src modules [7809, 7810, 7811, 7812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7809 import add_7809
from module_7810 import subtract_7810
from module_7811 import multiply_7811
from module_7812 import divide_7812

def test_add_7809():
    assert add_7809(2, 3) == 5

def test_subtract_7810():
    assert subtract_7810(10, 4) == 6

def test_multiply_7811():
    assert multiply_7811(3, 7) == 21

def test_divide_7812():
    assert divide_7812(10, 2) == 5.0
