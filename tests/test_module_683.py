"""Tests for test module 683 — covers src modules [2729, 2730, 2731, 2732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2729 import add_2729
from module_2730 import subtract_2730
from module_2731 import multiply_2731
from module_2732 import divide_2732

def test_add_2729():
    assert add_2729(2, 3) == 5

def test_subtract_2730():
    assert subtract_2730(10, 4) == 6

def test_multiply_2731():
    assert multiply_2731(3, 7) == 21

def test_divide_2732():
    assert divide_2732(10, 2) == 5.0
