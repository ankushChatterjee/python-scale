"""Tests for test module 1993 — covers src modules [7969, 7970, 7971, 7972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7969 import add_7969
from module_7970 import subtract_7970
from module_7971 import multiply_7971
from module_7972 import divide_7972

def test_add_7969():
    assert add_7969(2, 3) == 5

def test_subtract_7970():
    assert subtract_7970(10, 4) == 6

def test_multiply_7971():
    assert multiply_7971(3, 7) == 21

def test_divide_7972():
    assert divide_7972(10, 2) == 5.0
