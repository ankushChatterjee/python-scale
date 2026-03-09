"""Tests for test module 1199 — covers src modules [4793, 4794, 4795, 4796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4793 import add_4793
from module_4794 import subtract_4794
from module_4795 import multiply_4795
from module_4796 import divide_4796

def test_add_4793():
    assert add_4793(2, 3) == 5

def test_subtract_4794():
    assert subtract_4794(10, 4) == 6

def test_multiply_4795():
    assert multiply_4795(3, 7) == 21

def test_divide_4796():
    assert divide_4796(10, 2) == 5.0
