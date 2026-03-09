"""Tests for test module 1413 — covers src modules [5649, 5650, 5651, 5652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5649 import add_5649
from module_5650 import subtract_5650
from module_5651 import multiply_5651
from module_5652 import divide_5652

def test_add_5649():
    assert add_5649(2, 3) == 5

def test_subtract_5650():
    assert subtract_5650(10, 4) == 6

def test_multiply_5651():
    assert multiply_5651(3, 7) == 21

def test_divide_5652():
    assert divide_5652(10, 2) == 5.0
