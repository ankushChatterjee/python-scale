"""Tests for test module 1121 — covers src modules [4481, 4482, 4483, 4484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4481 import add_4481
from module_4482 import subtract_4482
from module_4483 import multiply_4483
from module_4484 import divide_4484

def test_add_4481():
    assert add_4481(2, 3) == 5

def test_subtract_4482():
    assert subtract_4482(10, 4) == 6

def test_multiply_4483():
    assert multiply_4483(3, 7) == 21

def test_divide_4484():
    assert divide_4484(10, 2) == 5.0
