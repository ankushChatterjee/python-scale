"""Tests for test module 961 — covers src modules [3841, 3842, 3843, 3844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3841 import add_3841
from module_3842 import subtract_3842
from module_3843 import multiply_3843
from module_3844 import divide_3844

def test_add_3841():
    assert add_3841(2, 3) == 5

def test_subtract_3842():
    assert subtract_3842(10, 4) == 6

def test_multiply_3843():
    assert multiply_3843(3, 7) == 21

def test_divide_3844():
    assert divide_3844(10, 2) == 5.0
