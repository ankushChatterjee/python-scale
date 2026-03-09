"""Tests for test module 1743 — covers src modules [6969, 6970, 6971, 6972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6969 import add_6969
from module_6970 import subtract_6970
from module_6971 import multiply_6971
from module_6972 import divide_6972

def test_add_6969():
    assert add_6969(2, 3) == 5

def test_subtract_6970():
    assert subtract_6970(10, 4) == 6

def test_multiply_6971():
    assert multiply_6971(3, 7) == 21

def test_divide_6972():
    assert divide_6972(10, 2) == 5.0
