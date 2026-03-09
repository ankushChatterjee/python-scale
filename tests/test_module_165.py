"""Tests for test module 165 — covers src modules [657, 658, 659, 660]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_657 import add_657
from module_658 import subtract_658
from module_659 import multiply_659
from module_660 import divide_660

def test_add_657():
    assert add_657(2, 3) == 5

def test_subtract_658():
    assert subtract_658(10, 4) == 6

def test_multiply_659():
    assert multiply_659(3, 7) == 21

def test_divide_660():
    assert divide_660(10, 2) == 5.0
