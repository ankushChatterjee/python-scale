"""Tests for test module 2429 — covers src modules [9713, 9714, 9715, 9716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9713 import add_9713
from module_9714 import subtract_9714
from module_9715 import multiply_9715
from module_9716 import divide_9716

def test_add_9713():
    assert add_9713(2, 3) == 5

def test_subtract_9714():
    assert subtract_9714(10, 4) == 6

def test_multiply_9715():
    assert multiply_9715(3, 7) == 21

def test_divide_9716():
    assert divide_9716(10, 2) == 5.0
