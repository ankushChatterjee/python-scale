"""Tests for test module 163 — covers src modules [649, 650, 651, 652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_649 import add_649
from module_650 import subtract_650
from module_651 import multiply_651
from module_652 import divide_652

def test_add_649():
    assert add_649(2, 3) == 5

def test_subtract_650():
    assert subtract_650(10, 4) == 6

def test_multiply_651():
    assert multiply_651(3, 7) == 21

def test_divide_652():
    assert divide_652(10, 2) == 5.0
