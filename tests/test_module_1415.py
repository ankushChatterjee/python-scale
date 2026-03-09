"""Tests for test module 1415 — covers src modules [5657, 5658, 5659, 5660]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5657 import add_5657
from module_5658 import subtract_5658
from module_5659 import multiply_5659
from module_5660 import divide_5660

def test_add_5657():
    assert add_5657(2, 3) == 5

def test_subtract_5658():
    assert subtract_5658(10, 4) == 6

def test_multiply_5659():
    assert multiply_5659(3, 7) == 21

def test_divide_5660():
    assert divide_5660(10, 2) == 5.0
