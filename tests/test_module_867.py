"""Tests for test module 867 — covers src modules [3465, 3466, 3467, 3468]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3465 import add_3465
from module_3466 import subtract_3466
from module_3467 import multiply_3467
from module_3468 import divide_3468

def test_add_3465():
    assert add_3465(2, 3) == 5

def test_subtract_3466():
    assert subtract_3466(10, 4) == 6

def test_multiply_3467():
    assert multiply_3467(3, 7) == 21

def test_divide_3468():
    assert divide_3468(10, 2) == 5.0
