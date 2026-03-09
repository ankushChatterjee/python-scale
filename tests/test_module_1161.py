"""Tests for test module 1161 — covers src modules [4641, 4642, 4643, 4644]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4641 import add_4641
from module_4642 import subtract_4642
from module_4643 import multiply_4643
from module_4644 import divide_4644

def test_add_4641():
    assert add_4641(2, 3) == 5

def test_subtract_4642():
    assert subtract_4642(10, 4) == 6

def test_multiply_4643():
    assert multiply_4643(3, 7) == 21

def test_divide_4644():
    assert divide_4644(10, 2) == 5.0
