"""Tests for test module 871 — covers src modules [3481, 3482, 3483, 3484]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3481 import add_3481
from module_3482 import subtract_3482
from module_3483 import multiply_3483
from module_3484 import divide_3484

def test_add_3481():
    assert add_3481(2, 3) == 5

def test_subtract_3482():
    assert subtract_3482(10, 4) == 6

def test_multiply_3483():
    assert multiply_3483(3, 7) == 21

def test_divide_3484():
    assert divide_3484(10, 2) == 5.0
