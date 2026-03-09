"""Tests for test module 1183 — covers src modules [4729, 4730, 4731, 4732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4729 import add_4729
from module_4730 import subtract_4730
from module_4731 import multiply_4731
from module_4732 import divide_4732

def test_add_4729():
    assert add_4729(2, 3) == 5

def test_subtract_4730():
    assert subtract_4730(10, 4) == 6

def test_multiply_4731():
    assert multiply_4731(3, 7) == 21

def test_divide_4732():
    assert divide_4732(10, 2) == 5.0
