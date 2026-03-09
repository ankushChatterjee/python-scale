"""Tests for test module 2395 — covers src modules [9577, 9578, 9579, 9580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9577 import add_9577
from module_9578 import subtract_9578
from module_9579 import multiply_9579
from module_9580 import divide_9580

def test_add_9577():
    assert add_9577(2, 3) == 5

def test_subtract_9578():
    assert subtract_9578(10, 4) == 6

def test_multiply_9579():
    assert multiply_9579(3, 7) == 21

def test_divide_9580():
    assert divide_9580(10, 2) == 5.0
