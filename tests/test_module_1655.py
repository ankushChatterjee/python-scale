"""Tests for test module 1655 — covers src modules [6617, 6618, 6619, 6620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6617 import add_6617
from module_6618 import subtract_6618
from module_6619 import multiply_6619
from module_6620 import divide_6620

def test_add_6617():
    assert add_6617(2, 3) == 5

def test_subtract_6618():
    assert subtract_6618(10, 4) == 6

def test_multiply_6619():
    assert multiply_6619(3, 7) == 21

def test_divide_6620():
    assert divide_6620(10, 2) == 5.0
