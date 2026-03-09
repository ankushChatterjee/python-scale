"""Tests for test module 431 — covers src modules [1721, 1722, 1723, 1724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1721 import add_1721
from module_1722 import subtract_1722
from module_1723 import multiply_1723
from module_1724 import divide_1724

def test_add_1721():
    assert add_1721(2, 3) == 5

def test_subtract_1722():
    assert subtract_1722(10, 4) == 6

def test_multiply_1723():
    assert multiply_1723(3, 7) == 21

def test_divide_1724():
    assert divide_1724(10, 2) == 5.0
