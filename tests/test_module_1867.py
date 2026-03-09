"""Tests for test module 1867 — covers src modules [7465, 7466, 7467, 7468]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7465 import add_7465
from module_7466 import subtract_7466
from module_7467 import multiply_7467
from module_7468 import divide_7468

def test_add_7465():
    assert add_7465(2, 3) == 5

def test_subtract_7466():
    assert subtract_7466(10, 4) == 6

def test_multiply_7467():
    assert multiply_7467(3, 7) == 21

def test_divide_7468():
    assert divide_7468(10, 2) == 5.0
