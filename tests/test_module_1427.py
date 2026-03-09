"""Tests for test module 1427 — covers src modules [5705, 5706, 5707, 5708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5705 import add_5705
from module_5706 import subtract_5706
from module_5707 import multiply_5707
from module_5708 import divide_5708

def test_add_5705():
    assert add_5705(2, 3) == 5

def test_subtract_5706():
    assert subtract_5706(10, 4) == 6

def test_multiply_5707():
    assert multiply_5707(3, 7) == 21

def test_divide_5708():
    assert divide_5708(10, 2) == 5.0
