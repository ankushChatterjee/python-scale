"""Tests for test module 1467 — covers src modules [5865, 5866, 5867, 5868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5865 import add_5865
from module_5866 import subtract_5866
from module_5867 import multiply_5867
from module_5868 import divide_5868

def test_add_5865():
    assert add_5865(2, 3) == 5

def test_subtract_5866():
    assert subtract_5866(10, 4) == 6

def test_multiply_5867():
    assert multiply_5867(3, 7) == 21

def test_divide_5868():
    assert divide_5868(10, 2) == 5.0
