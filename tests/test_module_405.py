"""Tests for test module 405 — covers src modules [1617, 1618, 1619, 1620]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1617 import add_1617
from module_1618 import subtract_1618
from module_1619 import multiply_1619
from module_1620 import divide_1620

def test_add_1617():
    assert add_1617(2, 3) == 5

def test_subtract_1618():
    assert subtract_1618(10, 4) == 6

def test_multiply_1619():
    assert multiply_1619(3, 7) == 21

def test_divide_1620():
    assert divide_1620(10, 2) == 5.0
