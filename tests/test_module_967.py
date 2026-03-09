"""Tests for test module 967 — covers src modules [3865, 3866, 3867, 3868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3865 import add_3865
from module_3866 import subtract_3866
from module_3867 import multiply_3867
from module_3868 import divide_3868

def test_add_3865():
    assert add_3865(2, 3) == 5

def test_subtract_3866():
    assert subtract_3866(10, 4) == 6

def test_multiply_3867():
    assert multiply_3867(3, 7) == 21

def test_divide_3868():
    assert divide_3868(10, 2) == 5.0
