"""Tests for test module 2117 — covers src modules [8465, 8466, 8467, 8468]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8465 import add_8465
from module_8466 import subtract_8466
from module_8467 import multiply_8467
from module_8468 import divide_8468

def test_add_8465():
    assert add_8465(2, 3) == 5

def test_subtract_8466():
    assert subtract_8466(10, 4) == 6

def test_multiply_8467():
    assert multiply_8467(3, 7) == 21

def test_divide_8468():
    assert divide_8468(10, 2) == 5.0
