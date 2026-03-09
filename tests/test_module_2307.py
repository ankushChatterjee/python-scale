"""Tests for test module 2307 — covers src modules [9225, 9226, 9227, 9228]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9225 import add_9225
from module_9226 import subtract_9226
from module_9227 import multiply_9227
from module_9228 import divide_9228

def test_add_9225():
    assert add_9225(2, 3) == 5

def test_subtract_9226():
    assert subtract_9226(10, 4) == 6

def test_multiply_9227():
    assert multiply_9227(3, 7) == 21

def test_divide_9228():
    assert divide_9228(10, 2) == 5.0
