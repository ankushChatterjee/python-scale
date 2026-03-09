"""Tests for test module 1243 — covers src modules [4969, 4970, 4971, 4972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4969 import add_4969
from module_4970 import subtract_4970
from module_4971 import multiply_4971
from module_4972 import divide_4972

def test_add_4969():
    assert add_4969(2, 3) == 5

def test_subtract_4970():
    assert subtract_4970(10, 4) == 6

def test_multiply_4971():
    assert multiply_4971(3, 7) == 21

def test_divide_4972():
    assert divide_4972(10, 2) == 5.0
