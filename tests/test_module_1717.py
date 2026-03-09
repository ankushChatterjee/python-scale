"""Tests for test module 1717 — covers src modules [6865, 6866, 6867, 6868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6865 import add_6865
from module_6866 import subtract_6866
from module_6867 import multiply_6867
from module_6868 import divide_6868

def test_add_6865():
    assert add_6865(2, 3) == 5

def test_subtract_6866():
    assert subtract_6866(10, 4) == 6

def test_multiply_6867():
    assert multiply_6867(3, 7) == 21

def test_divide_6868():
    assert divide_6868(10, 2) == 5.0
