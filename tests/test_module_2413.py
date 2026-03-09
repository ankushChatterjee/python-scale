"""Tests for test module 2413 — covers src modules [9649, 9650, 9651, 9652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9649 import add_9649
from module_9650 import subtract_9650
from module_9651 import multiply_9651
from module_9652 import divide_9652

def test_add_9649():
    assert add_9649(2, 3) == 5

def test_subtract_9650():
    assert subtract_9650(10, 4) == 6

def test_multiply_9651():
    assert multiply_9651(3, 7) == 21

def test_divide_9652():
    assert divide_9652(10, 2) == 5.0
