"""Tests for test module 1949 — covers src modules [7793, 7794, 7795, 7796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7793 import add_7793
from module_7794 import subtract_7794
from module_7795 import multiply_7795
from module_7796 import divide_7796

def test_add_7793():
    assert add_7793(2, 3) == 5

def test_subtract_7794():
    assert subtract_7794(10, 4) == 6

def test_multiply_7795():
    assert multiply_7795(3, 7) == 21

def test_divide_7796():
    assert divide_7796(10, 2) == 5.0
