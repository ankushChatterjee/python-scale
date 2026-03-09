"""Tests for test module 199 — covers src modules [793, 794, 795, 796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_793 import add_793
from module_794 import subtract_794
from module_795 import multiply_795
from module_796 import divide_796

def test_add_793():
    assert add_793(2, 3) == 5

def test_subtract_794():
    assert subtract_794(10, 4) == 6

def test_multiply_795():
    assert multiply_795(3, 7) == 21

def test_divide_796():
    assert divide_796(10, 2) == 5.0
