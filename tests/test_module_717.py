"""Tests for test module 717 — covers src modules [2865, 2866, 2867, 2868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2865 import add_2865
from module_2866 import subtract_2866
from module_2867 import multiply_2867
from module_2868 import divide_2868

def test_add_2865():
    assert add_2865(2, 3) == 5

def test_subtract_2866():
    assert subtract_2866(10, 4) == 6

def test_multiply_2867():
    assert multiply_2867(3, 7) == 21

def test_divide_2868():
    assert divide_2868(10, 2) == 5.0
