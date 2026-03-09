"""Tests for test module 1663 — covers src modules [6649, 6650, 6651, 6652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6649 import add_6649
from module_6650 import subtract_6650
from module_6651 import multiply_6651
from module_6652 import divide_6652

def test_add_6649():
    assert add_6649(2, 3) == 5

def test_subtract_6650():
    assert subtract_6650(10, 4) == 6

def test_multiply_6651():
    assert multiply_6651(3, 7) == 21

def test_divide_6652():
    assert divide_6652(10, 2) == 5.0
