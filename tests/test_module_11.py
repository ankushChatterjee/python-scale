"""Tests for test module 11 — covers src modules [41, 42, 43, 44]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_41 import add_41
from module_42 import subtract_42
from module_43 import multiply_43
from module_44 import divide_44

def test_add_41():
    assert add_41(2, 3) == 5

def test_subtract_42():
    assert subtract_42(10, 4) == 6

def test_multiply_43():
    assert multiply_43(3, 7) == 21

def test_divide_44():
    assert divide_44(10, 2) == 5.0
