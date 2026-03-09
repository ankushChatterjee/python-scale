"""Tests for test module 731 — covers src modules [2921, 2922, 2923, 2924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2921 import add_2921
from module_2922 import subtract_2922
from module_2923 import multiply_2923
from module_2924 import divide_2924

def test_add_2921():
    assert add_2921(2, 3) == 5

def test_subtract_2922():
    assert subtract_2922(10, 4) == 6

def test_multiply_2923():
    assert multiply_2923(3, 7) == 21

def test_divide_2924():
    assert divide_2924(10, 2) == 5.0
