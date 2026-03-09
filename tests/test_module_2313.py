"""Tests for test module 2313 — covers src modules [9249, 9250, 9251, 9252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9249 import add_9249
from module_9250 import subtract_9250
from module_9251 import multiply_9251
from module_9252 import divide_9252

def test_add_9249():
    assert add_9249(2, 3) == 5

def test_subtract_9250():
    assert subtract_9250(10, 4) == 6

def test_multiply_9251():
    assert multiply_9251(3, 7) == 21

def test_divide_9252():
    assert divide_9252(10, 2) == 5.0
