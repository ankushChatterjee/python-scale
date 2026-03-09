"""Tests for test module 231 — covers src modules [921, 922, 923, 924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_921 import add_921
from module_922 import subtract_922
from module_923 import multiply_923
from module_924 import divide_924

def test_add_921():
    assert add_921(2, 3) == 5

def test_subtract_922():
    assert subtract_922(10, 4) == 6

def test_multiply_923():
    assert multiply_923(3, 7) == 21

def test_divide_924():
    assert divide_924(10, 2) == 5.0
