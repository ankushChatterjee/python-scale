"""Tests for test module 151 — covers src modules [601, 602, 603, 604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_601 import add_601
from module_602 import subtract_602
from module_603 import multiply_603
from module_604 import divide_604

def test_add_601():
    assert add_601(2, 3) == 5

def test_subtract_602():
    assert subtract_602(10, 4) == 6

def test_multiply_603():
    assert multiply_603(3, 7) == 21

def test_divide_604():
    assert divide_604(10, 2) == 5.0
