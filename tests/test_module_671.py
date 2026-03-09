"""Tests for test module 671 — covers src modules [2681, 2682, 2683, 2684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2681 import add_2681
from module_2682 import subtract_2682
from module_2683 import multiply_2683
from module_2684 import divide_2684

def test_add_2681():
    assert add_2681(2, 3) == 5

def test_subtract_2682():
    assert subtract_2682(10, 4) == 6

def test_multiply_2683():
    assert multiply_2683(3, 7) == 21

def test_divide_2684():
    assert divide_2684(10, 2) == 5.0
