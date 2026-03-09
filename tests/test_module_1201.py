"""Tests for test module 1201 — covers src modules [4801, 4802, 4803, 4804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4801 import add_4801
from module_4802 import subtract_4802
from module_4803 import multiply_4803
from module_4804 import divide_4804

def test_add_4801():
    assert add_4801(2, 3) == 5

def test_subtract_4802():
    assert subtract_4802(10, 4) == 6

def test_multiply_4803():
    assert multiply_4803(3, 7) == 21

def test_divide_4804():
    assert divide_4804(10, 2) == 5.0
