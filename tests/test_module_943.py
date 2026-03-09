"""Tests for test module 943 — covers src modules [3769, 3770, 3771, 3772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3769 import add_3769
from module_3770 import subtract_3770
from module_3771 import multiply_3771
from module_3772 import divide_3772

def test_add_3769():
    assert add_3769(2, 3) == 5

def test_subtract_3770():
    assert subtract_3770(10, 4) == 6

def test_multiply_3771():
    assert multiply_3771(3, 7) == 21

def test_divide_3772():
    assert divide_3772(10, 2) == 5.0
