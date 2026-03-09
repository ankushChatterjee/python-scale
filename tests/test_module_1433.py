"""Tests for test module 1433 — covers src modules [5729, 5730, 5731, 5732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5729 import add_5729
from module_5730 import subtract_5730
from module_5731 import multiply_5731
from module_5732 import divide_5732

def test_add_5729():
    assert add_5729(2, 3) == 5

def test_subtract_5730():
    assert subtract_5730(10, 4) == 6

def test_multiply_5731():
    assert multiply_5731(3, 7) == 21

def test_divide_5732():
    assert divide_5732(10, 2) == 5.0
