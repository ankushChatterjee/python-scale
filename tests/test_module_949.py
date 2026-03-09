"""Tests for test module 949 — covers src modules [3793, 3794, 3795, 3796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3793 import add_3793
from module_3794 import subtract_3794
from module_3795 import multiply_3795
from module_3796 import divide_3796

def test_add_3793():
    assert add_3793(2, 3) == 5

def test_subtract_3794():
    assert subtract_3794(10, 4) == 6

def test_multiply_3795():
    assert multiply_3795(3, 7) == 21

def test_divide_3796():
    assert divide_3796(10, 2) == 5.0
