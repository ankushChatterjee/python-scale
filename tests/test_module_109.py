"""Tests for test module 109 — covers src modules [433, 434, 435, 436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_433 import add_433
from module_434 import subtract_434
from module_435 import multiply_435
from module_436 import divide_436

def test_add_433():
    assert add_433(2, 3) == 5

def test_subtract_434():
    assert subtract_434(10, 4) == 6

def test_multiply_435():
    assert multiply_435(3, 7) == 21

def test_divide_436():
    assert divide_436(10, 2) == 5.0
