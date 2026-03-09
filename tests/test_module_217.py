"""Tests for test module 217 — covers src modules [865, 866, 867, 868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_865 import add_865
from module_866 import subtract_866
from module_867 import multiply_867
from module_868 import divide_868

def test_add_865():
    assert add_865(2, 3) == 5

def test_subtract_866():
    assert subtract_866(10, 4) == 6

def test_multiply_867():
    assert multiply_867(3, 7) == 21

def test_divide_868():
    assert divide_868(10, 2) == 5.0
