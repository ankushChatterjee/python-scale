"""Tests for test module 1969 — covers src modules [7873, 7874, 7875, 7876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7873 import add_7873
from module_7874 import subtract_7874
from module_7875 import multiply_7875
from module_7876 import divide_7876

def test_add_7873():
    assert add_7873(2, 3) == 5

def test_subtract_7874():
    assert subtract_7874(10, 4) == 6

def test_multiply_7875():
    assert multiply_7875(3, 7) == 21

def test_divide_7876():
    assert divide_7876(10, 2) == 5.0
