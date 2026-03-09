"""Tests for test module 1227 — covers src modules [4905, 4906, 4907, 4908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4905 import add_4905
from module_4906 import subtract_4906
from module_4907 import multiply_4907
from module_4908 import divide_4908

def test_add_4905():
    assert add_4905(2, 3) == 5

def test_subtract_4906():
    assert subtract_4906(10, 4) == 6

def test_multiply_4907():
    assert multiply_4907(3, 7) == 21

def test_divide_4908():
    assert divide_4908(10, 2) == 5.0
