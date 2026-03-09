"""Tests for test module 951 — covers src modules [3801, 3802, 3803, 3804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3801 import add_3801
from module_3802 import subtract_3802
from module_3803 import multiply_3803
from module_3804 import divide_3804

def test_add_3801():
    assert add_3801(2, 3) == 5

def test_subtract_3802():
    assert subtract_3802(10, 4) == 6

def test_multiply_3803():
    assert multiply_3803(3, 7) == 21

def test_divide_3804():
    assert divide_3804(10, 2) == 5.0
