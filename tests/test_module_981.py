"""Tests for test module 981 — covers src modules [3921, 3922, 3923, 3924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3921 import add_3921
from module_3922 import subtract_3922
from module_3923 import multiply_3923
from module_3924 import divide_3924

def test_add_3921():
    assert add_3921(2, 3) == 5

def test_subtract_3922():
    assert subtract_3922(10, 4) == 6

def test_multiply_3923():
    assert multiply_3923(3, 7) == 21

def test_divide_3924():
    assert divide_3924(10, 2) == 5.0
