"""Tests for test module 913 — covers src modules [3649, 3650, 3651, 3652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3649 import add_3649
from module_3650 import subtract_3650
from module_3651 import multiply_3651
from module_3652 import divide_3652

def test_add_3649():
    assert add_3649(2, 3) == 5

def test_subtract_3650():
    assert subtract_3650(10, 4) == 6

def test_multiply_3651():
    assert multiply_3651(3, 7) == 21

def test_divide_3652():
    assert divide_3652(10, 2) == 5.0
