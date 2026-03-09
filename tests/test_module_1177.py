"""Tests for test module 1177 — covers src modules [4705, 4706, 4707, 4708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4705 import add_4705
from module_4706 import subtract_4706
from module_4707 import multiply_4707
from module_4708 import divide_4708

def test_add_4705():
    assert add_4705(2, 3) == 5

def test_subtract_4706():
    assert subtract_4706(10, 4) == 6

def test_multiply_4707():
    assert multiply_4707(3, 7) == 21

def test_divide_4708():
    assert divide_4708(10, 2) == 5.0
