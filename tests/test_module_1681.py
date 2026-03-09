"""Tests for test module 1681 — covers src modules [6721, 6722, 6723, 6724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6721 import add_6721
from module_6722 import subtract_6722
from module_6723 import multiply_6723
from module_6724 import divide_6724

def test_add_6721():
    assert add_6721(2, 3) == 5

def test_subtract_6722():
    assert subtract_6722(10, 4) == 6

def test_multiply_6723():
    assert multiply_6723(3, 7) == 21

def test_divide_6724():
    assert divide_6724(10, 2) == 5.0
