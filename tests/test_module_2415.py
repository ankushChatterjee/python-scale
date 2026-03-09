"""Tests for test module 2415 — covers src modules [9657, 9658, 9659, 9660]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9657 import add_9657
from module_9658 import subtract_9658
from module_9659 import multiply_9659
from module_9660 import divide_9660

def test_add_9657():
    assert add_9657(2, 3) == 5

def test_subtract_9658():
    assert subtract_9658(10, 4) == 6

def test_multiply_9659():
    assert multiply_9659(3, 7) == 21

def test_divide_9660():
    assert divide_9660(10, 2) == 5.0
