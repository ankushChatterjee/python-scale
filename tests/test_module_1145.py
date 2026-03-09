"""Tests for test module 1145 — covers src modules [4577, 4578, 4579, 4580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4577 import add_4577
from module_4578 import subtract_4578
from module_4579 import multiply_4579
from module_4580 import divide_4580

def test_add_4577():
    assert add_4577(2, 3) == 5

def test_subtract_4578():
    assert subtract_4578(10, 4) == 6

def test_multiply_4579():
    assert multiply_4579(3, 7) == 21

def test_divide_4580():
    assert divide_4580(10, 2) == 5.0
