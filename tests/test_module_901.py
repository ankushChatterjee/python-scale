"""Tests for test module 901 — covers src modules [3601, 3602, 3603, 3604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3601 import add_3601
from module_3602 import subtract_3602
from module_3603 import multiply_3603
from module_3604 import divide_3604

def test_add_3601():
    assert add_3601(2, 3) == 5

def test_subtract_3602():
    assert subtract_3602(10, 4) == 6

def test_multiply_3603():
    assert multiply_3603(3, 7) == 21

def test_divide_3604():
    assert divide_3604(10, 2) == 5.0
