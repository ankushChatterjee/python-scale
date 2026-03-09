"""Tests for test module 613 — covers src modules [2449, 2450, 2451, 2452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2449 import add_2449
from module_2450 import subtract_2450
from module_2451 import multiply_2451
from module_2452 import divide_2452

def test_add_2449():
    assert add_2449(2, 3) == 5

def test_subtract_2450():
    assert subtract_2450(10, 4) == 6

def test_multiply_2451():
    assert multiply_2451(3, 7) == 21

def test_divide_2452():
    assert divide_2452(10, 2) == 5.0
