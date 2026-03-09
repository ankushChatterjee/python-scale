"""Tests for test module 931 — covers src modules [3721, 3722, 3723, 3724]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3721 import add_3721
from module_3722 import subtract_3722
from module_3723 import multiply_3723
from module_3724 import divide_3724

def test_add_3721():
    assert add_3721(2, 3) == 5

def test_subtract_3722():
    assert subtract_3722(10, 4) == 6

def test_multiply_3723():
    assert multiply_3723(3, 7) == 21

def test_divide_3724():
    assert divide_3724(10, 2) == 5.0
