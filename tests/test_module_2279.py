"""Tests for test module 2279 — covers src modules [9113, 9114, 9115, 9116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9113 import add_9113
from module_9114 import subtract_9114
from module_9115 import multiply_9115
from module_9116 import divide_9116

def test_add_9113():
    assert add_9113(2, 3) == 5

def test_subtract_9114():
    assert subtract_9114(10, 4) == 6

def test_multiply_9115():
    assert multiply_9115(3, 7) == 21

def test_divide_9116():
    assert divide_9116(10, 2) == 5.0
