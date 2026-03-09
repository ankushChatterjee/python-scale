"""Tests for test module 1871 — covers src modules [7481, 7482, 7483, 7484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7481 import add_7481
from module_7482 import subtract_7482
from module_7483 import multiply_7483
from module_7484 import divide_7484

def test_add_7481():
    assert add_7481(2, 3) == 5

def test_subtract_7482():
    assert subtract_7482(10, 4) == 6

def test_multiply_7483():
    assert multiply_7483(3, 7) == 21

def test_divide_7484():
    assert divide_7484(10, 2) == 5.0
