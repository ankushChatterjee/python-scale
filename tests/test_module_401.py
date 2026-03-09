"""Tests for test module 401 — covers src modules [1601, 1602, 1603, 1604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1601 import add_1601
from module_1602 import subtract_1602
from module_1603 import multiply_1603
from module_1604 import divide_1604

def test_add_1601():
    assert add_1601(2, 3) == 5

def test_subtract_1602():
    assert subtract_1602(10, 4) == 6

def test_multiply_1603():
    assert multiply_1603(3, 7) == 21

def test_divide_1604():
    assert divide_1604(10, 2) == 5.0
