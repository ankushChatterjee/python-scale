"""Tests for test module 121 — covers src modules [481, 482, 483, 484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_481 import add_481
from module_482 import subtract_482
from module_483 import multiply_483
from module_484 import divide_484

def test_add_481():
    assert add_481(2, 3) == 5

def test_subtract_482():
    assert subtract_482(10, 4) == 6

def test_multiply_483():
    assert multiply_483(3, 7) == 21

def test_divide_484():
    assert divide_484(10, 2) == 5.0
