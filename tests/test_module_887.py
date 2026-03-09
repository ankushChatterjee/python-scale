"""Tests for test module 887 — covers src modules [3545, 3546, 3547, 3548]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3545 import add_3545
from module_3546 import subtract_3546
from module_3547 import multiply_3547
from module_3548 import divide_3548

def test_add_3545():
    assert add_3545(2, 3) == 5

def test_subtract_3546():
    assert subtract_3546(10, 4) == 6

def test_multiply_3547():
    assert multiply_3547(3, 7) == 21

def test_divide_3548():
    assert divide_3548(10, 2) == 5.0
