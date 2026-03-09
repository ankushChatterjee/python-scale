"""Tests for test module 2259 — covers src modules [9033, 9034, 9035, 9036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9033 import add_9033
from module_9034 import subtract_9034
from module_9035 import multiply_9035
from module_9036 import divide_9036

def test_add_9033():
    assert add_9033(2, 3) == 5

def test_subtract_9034():
    assert subtract_9034(10, 4) == 6

def test_multiply_9035():
    assert multiply_9035(3, 7) == 21

def test_divide_9036():
    assert divide_9036(10, 2) == 5.0
