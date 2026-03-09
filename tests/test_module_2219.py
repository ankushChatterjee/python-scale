"""Tests for test module 2219 — covers src modules [8873, 8874, 8875, 8876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8873 import add_8873
from module_8874 import subtract_8874
from module_8875 import multiply_8875
from module_8876 import divide_8876

def test_add_8873():
    assert add_8873(2, 3) == 5

def test_subtract_8874():
    assert subtract_8874(10, 4) == 6

def test_multiply_8875():
    assert multiply_8875(3, 7) == 21

def test_divide_8876():
    assert divide_8876(10, 2) == 5.0
