"""Tests for test module 621 — covers src modules [2481, 2482, 2483, 2484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2481 import add_2481
from module_2482 import subtract_2482
from module_2483 import multiply_2483
from module_2484 import divide_2484

def test_add_2481():
    assert add_2481(2, 3) == 5

def test_subtract_2482():
    assert subtract_2482(10, 4) == 6

def test_multiply_2483():
    assert multiply_2483(3, 7) == 21

def test_divide_2484():
    assert divide_2484(10, 2) == 5.0
