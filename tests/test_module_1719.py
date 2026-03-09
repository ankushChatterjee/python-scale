"""Tests for test module 1719 — covers src modules [6873, 6874, 6875, 6876]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6873 import add_6873
from module_6874 import subtract_6874
from module_6875 import multiply_6875
from module_6876 import divide_6876

def test_add_6873():
    assert add_6873(2, 3) == 5

def test_subtract_6874():
    assert subtract_6874(10, 4) == 6

def test_multiply_6875():
    assert multiply_6875(3, 7) == 21

def test_divide_6876():
    assert divide_6876(10, 2) == 5.0
