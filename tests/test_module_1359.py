"""Tests for test module 1359 — covers src modules [5433, 5434, 5435, 5436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5433 import add_5433
from module_5434 import subtract_5434
from module_5435 import multiply_5435
from module_5436 import divide_5436

def test_add_5433():
    assert add_5433(2, 3) == 5

def test_subtract_5434():
    assert subtract_5434(10, 4) == 6

def test_multiply_5435():
    assert multiply_5435(3, 7) == 21

def test_divide_5436():
    assert divide_5436(10, 2) == 5.0
