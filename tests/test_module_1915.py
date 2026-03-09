"""Tests for test module 1915 — covers src modules [7657, 7658, 7659, 7660]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7657 import add_7657
from module_7658 import subtract_7658
from module_7659 import multiply_7659
from module_7660 import divide_7660

def test_add_7657():
    assert add_7657(2, 3) == 5

def test_subtract_7658():
    assert subtract_7658(10, 4) == 6

def test_multiply_7659():
    assert multiply_7659(3, 7) == 21

def test_divide_7660():
    assert divide_7660(10, 2) == 5.0
