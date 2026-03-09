"""Tests for test module 2467 — covers src modules [9865, 9866, 9867, 9868]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9865 import add_9865
from module_9866 import subtract_9866
from module_9867 import multiply_9867
from module_9868 import divide_9868

def test_add_9865():
    assert add_9865(2, 3) == 5

def test_subtract_9866():
    assert subtract_9866(10, 4) == 6

def test_multiply_9867():
    assert multiply_9867(3, 7) == 21

def test_divide_9868():
    assert divide_9868(10, 2) == 5.0
