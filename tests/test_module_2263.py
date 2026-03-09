"""Tests for test module 2263 — covers src modules [9049, 9050, 9051, 9052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9049 import add_9049
from module_9050 import subtract_9050
from module_9051 import multiply_9051
from module_9052 import divide_9052

def test_add_9049():
    assert add_9049(2, 3) == 5

def test_subtract_9050():
    assert subtract_9050(10, 4) == 6

def test_multiply_9051():
    assert multiply_9051(3, 7) == 21

def test_divide_9052():
    assert divide_9052(10, 2) == 5.0
