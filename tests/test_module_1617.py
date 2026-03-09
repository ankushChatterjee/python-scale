"""Tests for test module 1617 — covers src modules [6465, 6466, 6467, 6468]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6465 import add_6465
from module_6466 import subtract_6466
from module_6467 import multiply_6467
from module_6468 import divide_6468

def test_add_6465():
    assert add_6465(2, 3) == 5

def test_subtract_6466():
    assert subtract_6466(10, 4) == 6

def test_multiply_6467():
    assert multiply_6467(3, 7) == 21

def test_divide_6468():
    assert divide_6468(10, 2) == 5.0
