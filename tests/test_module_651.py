"""Tests for test module 651 — covers src modules [2601, 2602, 2603, 2604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2601 import add_2601
from module_2602 import subtract_2602
from module_2603 import multiply_2603
from module_2604 import divide_2604

def test_add_2601():
    assert add_2601(2, 3) == 5

def test_subtract_2602():
    assert subtract_2602(10, 4) == 6

def test_multiply_2603():
    assert multiply_2603(3, 7) == 21

def test_divide_2604():
    assert divide_2604(10, 2) == 5.0
