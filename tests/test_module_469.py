"""Tests for test module 469 — covers src modules [1873, 1874, 1875, 1876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1873 import add_1873
from module_1874 import subtract_1874
from module_1875 import multiply_1875
from module_1876 import divide_1876

def test_add_1873():
    assert add_1873(2, 3) == 5

def test_subtract_1874():
    assert subtract_1874(10, 4) == 6

def test_multiply_1875():
    assert multiply_1875(3, 7) == 21

def test_divide_1876():
    assert divide_1876(10, 2) == 5.0
