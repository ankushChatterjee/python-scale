"""Tests for test module 117 — covers src modules [465, 466, 467, 468]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_465 import add_465
from module_466 import subtract_466
from module_467 import multiply_467
from module_468 import divide_468

def test_add_465():
    assert add_465(2, 3) == 5

def test_subtract_466():
    assert subtract_466(10, 4) == 6

def test_multiply_467():
    assert multiply_467(3, 7) == 21

def test_divide_468():
    assert divide_468(10, 2) == 5.0
