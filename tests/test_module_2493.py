"""Tests for test module 2493 — covers src modules [9969, 9970, 9971, 9972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9969 import add_9969
from module_9970 import subtract_9970
from module_9971 import multiply_9971
from module_9972 import divide_9972

def test_add_9969():
    assert add_9969(2, 3) == 5

def test_subtract_9970():
    assert subtract_9970(10, 4) == 6

def test_multiply_9971():
    assert multiply_9971(3, 7) == 21

def test_divide_9972():
    assert divide_9972(10, 2) == 5.0
