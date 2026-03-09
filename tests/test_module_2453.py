"""Tests for test module 2453 — covers src modules [9809, 9810, 9811, 9812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9809 import add_9809
from module_9810 import subtract_9810
from module_9811 import multiply_9811
from module_9812 import divide_9812

def test_add_9809():
    assert add_9809(2, 3) == 5

def test_subtract_9810():
    assert subtract_9810(10, 4) == 6

def test_multiply_9811():
    assert multiply_9811(3, 7) == 21

def test_divide_9812():
    assert divide_9812(10, 2) == 5.0
