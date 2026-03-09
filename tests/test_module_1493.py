"""Tests for test module 1493 — covers src modules [5969, 5970, 5971, 5972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5969 import add_5969
from module_5970 import subtract_5970
from module_5971 import multiply_5971
from module_5972 import divide_5972

def test_add_5969():
    assert add_5969(2, 3) == 5

def test_subtract_5970():
    assert subtract_5970(10, 4) == 6

def test_multiply_5971():
    assert multiply_5971(3, 7) == 21

def test_divide_5972():
    assert divide_5972(10, 2) == 5.0
