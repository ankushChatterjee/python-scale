"""Tests for test module 1905 — covers src modules [7617, 7618, 7619, 7620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7617 import add_7617
from module_7618 import subtract_7618
from module_7619 import multiply_7619
from module_7620 import divide_7620

def test_add_7617():
    assert add_7617(2, 3) == 5

def test_subtract_7618():
    assert subtract_7618(10, 4) == 6

def test_multiply_7619():
    assert multiply_7619(3, 7) == 21

def test_divide_7620():
    assert divide_7620(10, 2) == 5.0
