"""Tests for test module 2265 — covers src modules [9057, 9058, 9059, 9060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9057 import add_9057
from module_9058 import subtract_9058
from module_9059 import multiply_9059
from module_9060 import divide_9060

def test_add_9057():
    assert add_9057(2, 3) == 5

def test_subtract_9058():
    assert subtract_9058(10, 4) == 6

def test_multiply_9059():
    assert multiply_9059(3, 7) == 21

def test_divide_9060():
    assert divide_9060(10, 2) == 5.0
