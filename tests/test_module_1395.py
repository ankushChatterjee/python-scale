"""Tests for test module 1395 — covers src modules [5577, 5578, 5579, 5580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5577 import add_5577
from module_5578 import subtract_5578
from module_5579 import multiply_5579
from module_5580 import divide_5580

def test_add_5577():
    assert add_5577(2, 3) == 5

def test_subtract_5578():
    assert subtract_5578(10, 4) == 6

def test_multiply_5579():
    assert multiply_5579(3, 7) == 21

def test_divide_5580():
    assert divide_5580(10, 2) == 5.0
