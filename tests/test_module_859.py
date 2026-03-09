"""Tests for test module 859 — covers src modules [3433, 3434, 3435, 3436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3433 import add_3433
from module_3434 import subtract_3434
from module_3435 import multiply_3435
from module_3436 import divide_3436

def test_add_3433():
    assert add_3433(2, 3) == 5

def test_subtract_3434():
    assert subtract_3434(10, 4) == 6

def test_multiply_3435():
    assert multiply_3435(3, 7) == 21

def test_divide_3436():
    assert divide_3436(10, 2) == 5.0
