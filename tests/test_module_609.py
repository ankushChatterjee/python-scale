"""Tests for test module 609 — covers src modules [2433, 2434, 2435, 2436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2433 import add_2433
from module_2434 import subtract_2434
from module_2435 import multiply_2435
from module_2436 import divide_2436

def test_add_2433():
    assert add_2433(2, 3) == 5

def test_subtract_2434():
    assert subtract_2434(10, 4) == 6

def test_multiply_2435():
    assert multiply_2435(3, 7) == 21

def test_divide_2436():
    assert divide_2436(10, 2) == 5.0
