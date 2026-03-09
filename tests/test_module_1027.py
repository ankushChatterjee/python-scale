"""Tests for test module 1027 — covers src modules [4105, 4106, 4107, 4108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4105 import add_4105
from module_4106 import subtract_4106
from module_4107 import multiply_4107
from module_4108 import divide_4108

def test_add_4105():
    assert add_4105(2, 3) == 5

def test_subtract_4106():
    assert subtract_4106(10, 4) == 6

def test_multiply_4107():
    assert multiply_4107(3, 7) == 21

def test_divide_4108():
    assert divide_4108(10, 2) == 5.0
