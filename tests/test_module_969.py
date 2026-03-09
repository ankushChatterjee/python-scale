"""Tests for test module 969 — covers src modules [3873, 3874, 3875, 3876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3873 import add_3873
from module_3874 import subtract_3874
from module_3875 import multiply_3875
from module_3876 import divide_3876

def test_add_3873():
    assert add_3873(2, 3) == 5

def test_subtract_3874():
    assert subtract_3874(10, 4) == 6

def test_multiply_3875():
    assert multiply_3875(3, 7) == 21

def test_divide_3876():
    assert divide_3876(10, 2) == 5.0
