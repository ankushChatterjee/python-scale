"""Tests for test module 1405 — covers src modules [5617, 5618, 5619, 5620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5617 import add_5617
from module_5618 import subtract_5618
from module_5619 import multiply_5619
from module_5620 import divide_5620

def test_add_5617():
    assert add_5617(2, 3) == 5

def test_subtract_5618():
    assert subtract_5618(10, 4) == 6

def test_multiply_5619():
    assert multiply_5619(3, 7) == 21

def test_divide_5620():
    assert divide_5620(10, 2) == 5.0
