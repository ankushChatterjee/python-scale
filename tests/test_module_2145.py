"""Tests for test module 2145 — covers src modules [8577, 8578, 8579, 8580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8577 import add_8577
from module_8578 import subtract_8578
from module_8579 import multiply_8579
from module_8580 import divide_8580

def test_add_8577():
    assert add_8577(2, 3) == 5

def test_subtract_8578():
    assert subtract_8578(10, 4) == 6

def test_multiply_8579():
    assert multiply_8579(3, 7) == 21

def test_divide_8580():
    assert divide_8580(10, 2) == 5.0
