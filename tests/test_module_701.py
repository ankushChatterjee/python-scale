"""Tests for test module 701 — covers src modules [2801, 2802, 2803, 2804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2801 import add_2801
from module_2802 import subtract_2802
from module_2803 import multiply_2803
from module_2804 import divide_2804

def test_add_2801():
    assert add_2801(2, 3) == 5

def test_subtract_2802():
    assert subtract_2802(10, 4) == 6

def test_multiply_2803():
    assert multiply_2803(3, 7) == 21

def test_divide_2804():
    assert divide_2804(10, 2) == 5.0
