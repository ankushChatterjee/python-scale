"""Tests for test module 1621 — covers src modules [6481, 6482, 6483, 6484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6481 import add_6481
from module_6482 import subtract_6482
from module_6483 import multiply_6483
from module_6484 import divide_6484

def test_add_6481():
    assert add_6481(2, 3) == 5

def test_subtract_6482():
    assert subtract_6482(10, 4) == 6

def test_multiply_6483():
    assert multiply_6483(3, 7) == 21

def test_divide_6484():
    assert divide_6484(10, 2) == 5.0
