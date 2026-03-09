"""Tests for test module 677 — covers src modules [2705, 2706, 2707, 2708]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2705 import add_2705
from module_2706 import subtract_2706
from module_2707 import multiply_2707
from module_2708 import divide_2708

def test_add_2705():
    assert add_2705(2, 3) == 5

def test_subtract_2706():
    assert subtract_2706(10, 4) == 6

def test_multiply_2707():
    assert multiply_2707(3, 7) == 21

def test_divide_2708():
    assert divide_2708(10, 2) == 5.0
