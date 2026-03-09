"""Tests for test module 1951 — covers src modules [7801, 7802, 7803, 7804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7801 import add_7801
from module_7802 import subtract_7802
from module_7803 import multiply_7803
from module_7804 import divide_7804

def test_add_7801():
    assert add_7801(2, 3) == 5

def test_subtract_7802():
    assert subtract_7802(10, 4) == 6

def test_multiply_7803():
    assert multiply_7803(3, 7) == 21

def test_divide_7804():
    assert divide_7804(10, 2) == 5.0
