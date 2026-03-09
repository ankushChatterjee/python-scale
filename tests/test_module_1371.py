"""Tests for test module 1371 — covers src modules [5481, 5482, 5483, 5484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5481 import add_5481
from module_5482 import subtract_5482
from module_5483 import multiply_5483
from module_5484 import divide_5484

def test_add_5481():
    assert add_5481(2, 3) == 5

def test_subtract_5482():
    assert subtract_5482(10, 4) == 6

def test_multiply_5483():
    assert multiply_5483(3, 7) == 21

def test_divide_5484():
    assert divide_5484(10, 2) == 5.0
