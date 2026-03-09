"""Tests for test module 2151 — covers src modules [8601, 8602, 8603, 8604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8601 import add_8601
from module_8602 import subtract_8602
from module_8603 import multiply_8603
from module_8604 import divide_8604

def test_add_8601():
    assert add_8601(2, 3) == 5

def test_subtract_8602():
    assert subtract_8602(10, 4) == 6

def test_multiply_8603():
    assert multiply_8603(3, 7) == 21

def test_divide_8604():
    assert divide_8604(10, 2) == 5.0
