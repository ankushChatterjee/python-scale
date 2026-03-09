"""Tests for test module 1363 — covers src modules [5449, 5450, 5451, 5452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5449 import add_5449
from module_5450 import subtract_5450
from module_5451 import multiply_5451
from module_5452 import divide_5452

def test_add_5449():
    assert add_5449(2, 3) == 5

def test_subtract_5450():
    assert subtract_5450(10, 4) == 6

def test_multiply_5451():
    assert multiply_5451(3, 7) == 21

def test_divide_5452():
    assert divide_5452(10, 2) == 5.0
