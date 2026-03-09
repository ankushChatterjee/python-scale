"""Tests for test module 1155 — covers src modules [4617, 4618, 4619, 4620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4617 import add_4617
from module_4618 import subtract_4618
from module_4619 import multiply_4619
from module_4620 import divide_4620

def test_add_4617():
    assert add_4617(2, 3) == 5

def test_subtract_4618():
    assert subtract_4618(10, 4) == 6

def test_multiply_4619():
    assert multiply_4619(3, 7) == 21

def test_divide_4620():
    assert divide_4620(10, 2) == 5.0
