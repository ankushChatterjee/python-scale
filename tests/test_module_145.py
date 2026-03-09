"""Tests for test module 145 — covers src modules [577, 578, 579, 580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_577 import add_577
from module_578 import subtract_578
from module_579 import multiply_579
from module_580 import divide_580

def test_add_577():
    assert add_577(2, 3) == 5

def test_subtract_578():
    assert subtract_578(10, 4) == 6

def test_multiply_579():
    assert multiply_579(3, 7) == 21

def test_divide_580():
    assert divide_580(10, 2) == 5.0
