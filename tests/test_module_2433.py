"""Tests for test module 2433 — covers src modules [9729, 9730, 9731, 9732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9729 import add_9729
from module_9730 import subtract_9730
from module_9731 import multiply_9731
from module_9732 import divide_9732

def test_add_9729():
    assert add_9729(2, 3) == 5

def test_subtract_9730():
    assert subtract_9730(10, 4) == 6

def test_multiply_9731():
    assert multiply_9731(3, 7) == 21

def test_divide_9732():
    assert divide_9732(10, 2) == 5.0
