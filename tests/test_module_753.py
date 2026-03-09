"""Tests for test module 753 — covers src modules [3009, 3010, 3011, 3012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3009 import add_3009
from module_3010 import subtract_3010
from module_3011 import multiply_3011
from module_3012 import divide_3012

def test_add_3009():
    assert add_3009(2, 3) == 5

def test_subtract_3010():
    assert subtract_3010(10, 4) == 6

def test_multiply_3011():
    assert multiply_3011(3, 7) == 21

def test_divide_3012():
    assert divide_3012(10, 2) == 5.0
