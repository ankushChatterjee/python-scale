"""Tests for test module 1967 — covers src modules [7865, 7866, 7867, 7868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7865 import add_7865
from module_7866 import subtract_7866
from module_7867 import multiply_7867
from module_7868 import divide_7868

def test_add_7865():
    assert add_7865(2, 3) == 5

def test_subtract_7866():
    assert subtract_7866(10, 4) == 6

def test_multiply_7867():
    assert multiply_7867(3, 7) == 21

def test_divide_7868():
    assert divide_7868(10, 2) == 5.0
