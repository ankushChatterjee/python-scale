"""Tests for test module 2217 — covers src modules [8865, 8866, 8867, 8868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8865 import add_8865
from module_8866 import subtract_8866
from module_8867 import multiply_8867
from module_8868 import divide_8868

def test_add_8865():
    assert add_8865(2, 3) == 5

def test_subtract_8866():
    assert subtract_8866(10, 4) == 6

def test_multiply_8867():
    assert multiply_8867(3, 7) == 21

def test_divide_8868():
    assert divide_8868(10, 2) == 5.0
