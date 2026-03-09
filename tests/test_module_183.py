"""Tests for test module 183 — covers src modules [729, 730, 731, 732]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_729 import add_729
from module_730 import subtract_730
from module_731 import multiply_731
from module_732 import divide_732

def test_add_729():
    assert add_729(2, 3) == 5

def test_subtract_730():
    assert subtract_730(10, 4) == 6

def test_multiply_731():
    assert multiply_731(3, 7) == 21

def test_divide_732():
    assert divide_732(10, 2) == 5.0
