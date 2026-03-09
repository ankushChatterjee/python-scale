"""Tests for test module 1651 — covers src modules [6601, 6602, 6603, 6604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6601 import add_6601
from module_6602 import subtract_6602
from module_6603 import multiply_6603
from module_6604 import divide_6604

def test_add_6601():
    assert add_6601(2, 3) == 5

def test_subtract_6602():
    assert subtract_6602(10, 4) == 6

def test_multiply_6603():
    assert multiply_6603(3, 7) == 21

def test_divide_6604():
    assert divide_6604(10, 2) == 5.0
