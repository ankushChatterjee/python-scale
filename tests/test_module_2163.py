"""Tests for test module 2163 — covers src modules [8649, 8650, 8651, 8652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8649 import add_8649
from module_8650 import subtract_8650
from module_8651 import multiply_8651
from module_8652 import divide_8652

def test_add_8649():
    assert add_8649(2, 3) == 5

def test_subtract_8650():
    assert subtract_8650(10, 4) == 6

def test_multiply_8651():
    assert multiply_8651(3, 7) == 21

def test_divide_8652():
    assert divide_8652(10, 2) == 5.0
