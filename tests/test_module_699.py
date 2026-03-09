"""Tests for test module 699 — covers src modules [2793, 2794, 2795, 2796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2793 import add_2793
from module_2794 import subtract_2794
from module_2795 import multiply_2795
from module_2796 import divide_2796

def test_add_2793():
    assert add_2793(2, 3) == 5

def test_subtract_2794():
    assert subtract_2794(10, 4) == 6

def test_multiply_2795():
    assert multiply_2795(3, 7) == 21

def test_divide_2796():
    assert divide_2796(10, 2) == 5.0
