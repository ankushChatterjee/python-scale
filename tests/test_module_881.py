"""Tests for test module 881 — covers src modules [3521, 3522, 3523, 3524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3521 import add_3521
from module_3522 import subtract_3522
from module_3523 import multiply_3523
from module_3524 import divide_3524

def test_add_3521():
    assert add_3521(2, 3) == 5

def test_subtract_3522():
    assert subtract_3522(10, 4) == 6

def test_multiply_3523():
    assert multiply_3523(3, 7) == 21

def test_divide_3524():
    assert divide_3524(10, 2) == 5.0
