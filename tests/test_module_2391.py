"""Tests for test module 2391 — covers src modules [9561, 9562, 9563, 9564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9561 import add_9561
from module_9562 import subtract_9562
from module_9563 import multiply_9563
from module_9564 import divide_9564

def test_add_9561():
    assert add_9561(2, 3) == 5

def test_subtract_9562():
    assert subtract_9562(10, 4) == 6

def test_multiply_9563():
    assert multiply_9563(3, 7) == 21

def test_divide_9564():
    assert divide_9564(10, 2) == 5.0
