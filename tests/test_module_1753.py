"""Tests for test module 1753 — covers src modules [7009, 7010, 7011, 7012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7009 import add_7009
from module_7010 import subtract_7010
from module_7011 import multiply_7011
from module_7012 import divide_7012

def test_add_7009():
    assert add_7009(2, 3) == 5

def test_subtract_7010():
    assert subtract_7010(10, 4) == 6

def test_multiply_7011():
    assert multiply_7011(3, 7) == 21

def test_divide_7012():
    assert divide_7012(10, 2) == 5.0
