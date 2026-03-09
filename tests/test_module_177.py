"""Tests for test module 177 — covers src modules [705, 706, 707, 708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_705 import add_705
from module_706 import subtract_706
from module_707 import multiply_707
from module_708 import divide_708

def test_add_705():
    assert add_705(2, 3) == 5

def test_subtract_706():
    assert subtract_706(10, 4) == 6

def test_multiply_707():
    assert multiply_707(3, 7) == 21

def test_divide_708():
    assert divide_708(10, 2) == 5.0
