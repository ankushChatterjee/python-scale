"""Tests for test module 1515 — covers src modules [6057, 6058, 6059, 6060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6057 import add_6057
from module_6058 import subtract_6058
from module_6059 import multiply_6059
from module_6060 import divide_6060

def test_add_6057():
    assert add_6057(2, 3) == 5

def test_subtract_6058():
    assert subtract_6058(10, 4) == 6

def test_multiply_6059():
    assert multiply_6059(3, 7) == 21

def test_divide_6060():
    assert divide_6060(10, 2) == 5.0
