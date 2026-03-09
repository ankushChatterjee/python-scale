"""Tests for test module 493 — covers src modules [1969, 1970, 1971, 1972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1969 import add_1969
from module_1970 import subtract_1970
from module_1971 import multiply_1971
from module_1972 import divide_1972

def test_add_1969():
    assert add_1969(2, 3) == 5

def test_subtract_1970():
    assert subtract_1970(10, 4) == 6

def test_multiply_1971():
    assert multiply_1971(3, 7) == 21

def test_divide_1972():
    assert divide_1972(10, 2) == 5.0
