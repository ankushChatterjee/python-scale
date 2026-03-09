"""Tests for test module 1117 — covers src modules [4465, 4466, 4467, 4468]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4465 import add_4465
from module_4466 import subtract_4466
from module_4467 import multiply_4467
from module_4468 import divide_4468

def test_add_4465():
    assert add_4465(2, 3) == 5

def test_subtract_4466():
    assert subtract_4466(10, 4) == 6

def test_multiply_4467():
    assert multiply_4467(3, 7) == 21

def test_divide_4468():
    assert divide_4468(10, 2) == 5.0
