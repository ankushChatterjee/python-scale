"""Tests for test module 2121 — covers src modules [8481, 8482, 8483, 8484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8481 import add_8481
from module_8482 import subtract_8482
from module_8483 import multiply_8483
from module_8484 import divide_8484

def test_add_8481():
    assert add_8481(2, 3) == 5

def test_subtract_8482():
    assert subtract_8482(10, 4) == 6

def test_multiply_8483():
    assert multiply_8483(3, 7) == 21

def test_divide_8484():
    assert divide_8484(10, 2) == 5.0
