"""Tests for test module 451 — covers src modules [1801, 1802, 1803, 1804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1801 import add_1801
from module_1802 import subtract_1802
from module_1803 import multiply_1803
from module_1804 import divide_1804

def test_add_1801():
    assert add_1801(2, 3) == 5

def test_subtract_1802():
    assert subtract_1802(10, 4) == 6

def test_multiply_1803():
    assert multiply_1803(3, 7) == 21

def test_divide_1804():
    assert divide_1804(10, 2) == 5.0
