"""Tests for test module 663 — covers src modules [2649, 2650, 2651, 2652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2649 import add_2649
from module_2650 import subtract_2650
from module_2651 import multiply_2651
from module_2652 import divide_2652

def test_add_2649():
    assert add_2649(2, 3) == 5

def test_subtract_2650():
    assert subtract_2650(10, 4) == 6

def test_multiply_2651():
    assert multiply_2651(3, 7) == 21

def test_divide_2652():
    assert divide_2652(10, 2) == 5.0
