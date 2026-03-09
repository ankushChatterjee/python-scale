"""Tests for test module 21 — covers src modules [81, 82, 83, 84]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_81 import add_81
from module_82 import subtract_82
from module_83 import multiply_83
from module_84 import divide_84

def test_add_81():
    assert add_81(2, 3) == 5

def test_subtract_82():
    assert subtract_82(10, 4) == 6

def test_multiply_83():
    assert multiply_83(3, 7) == 21

def test_divide_84():
    assert divide_84(10, 2) == 5.0
