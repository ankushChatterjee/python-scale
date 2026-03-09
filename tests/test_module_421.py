"""Tests for test module 421 — covers src modules [1681, 1682, 1683, 1684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1681 import add_1681
from module_1682 import subtract_1682
from module_1683 import multiply_1683
from module_1684 import divide_1684

def test_add_1681():
    assert add_1681(2, 3) == 5

def test_subtract_1682():
    assert subtract_1682(10, 4) == 6

def test_multiply_1683():
    assert multiply_1683(3, 7) == 21

def test_divide_1684():
    assert divide_1684(10, 2) == 5.0
