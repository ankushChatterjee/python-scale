"""Tests for test module 371 — covers src modules [1481, 1482, 1483, 1484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1481 import add_1481
from module_1482 import subtract_1482
from module_1483 import multiply_1483
from module_1484 import divide_1484

def test_add_1481():
    assert add_1481(2, 3) == 5

def test_subtract_1482():
    assert subtract_1482(10, 4) == 6

def test_multiply_1483():
    assert multiply_1483(3, 7) == 21

def test_divide_1484():
    assert divide_1484(10, 2) == 5.0
