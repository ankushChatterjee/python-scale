"""Tests for test module 1431 — covers src modules [5721, 5722, 5723, 5724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5721 import add_5721
from module_5722 import subtract_5722
from module_5723 import multiply_5723
from module_5724 import divide_5724

def test_add_5721():
    assert add_5721(2, 3) == 5

def test_subtract_5722():
    assert subtract_5722(10, 4) == 6

def test_multiply_5723():
    assert multiply_5723(3, 7) == 21

def test_divide_5724():
    assert divide_5724(10, 2) == 5.0
