"""Tests for test module 1109 — covers src modules [4433, 4434, 4435, 4436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4433 import add_4433
from module_4434 import subtract_4434
from module_4435 import multiply_4435
from module_4436 import divide_4436

def test_add_4433():
    assert add_4433(2, 3) == 5

def test_subtract_4434():
    assert subtract_4434(10, 4) == 6

def test_multiply_4435():
    assert multiply_4435(3, 7) == 21

def test_divide_4436():
    assert divide_4436(10, 2) == 5.0
