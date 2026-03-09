"""Tests for test module 1163 — covers src modules [4649, 4650, 4651, 4652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4649 import add_4649
from module_4650 import subtract_4650
from module_4651 import multiply_4651
from module_4652 import divide_4652

def test_add_4649():
    assert add_4649(2, 3) == 5

def test_subtract_4650():
    assert subtract_4650(10, 4) == 6

def test_multiply_4651():
    assert multiply_4651(3, 7) == 21

def test_divide_4652():
    assert divide_4652(10, 2) == 5.0
