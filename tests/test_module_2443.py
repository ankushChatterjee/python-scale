"""Tests for test module 2443 — covers src modules [9769, 9770, 9771, 9772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9769 import add_9769
from module_9770 import subtract_9770
from module_9771 import multiply_9771
from module_9772 import divide_9772

def test_add_9769():
    assert add_9769(2, 3) == 5

def test_subtract_9770():
    assert subtract_9770(10, 4) == 6

def test_multiply_9771():
    assert multiply_9771(3, 7) == 21

def test_divide_9772():
    assert divide_9772(10, 2) == 5.0
