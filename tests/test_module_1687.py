"""Tests for test module 1687 — covers src modules [6745, 6746, 6747, 6748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6745 import add_6745
from module_6746 import subtract_6746
from module_6747 import multiply_6747
from module_6748 import divide_6748

def test_add_6745():
    assert add_6745(2, 3) == 5

def test_subtract_6746():
    assert subtract_6746(10, 4) == 6

def test_multiply_6747():
    assert multiply_6747(3, 7) == 21

def test_divide_6748():
    assert divide_6748(10, 2) == 5.0
