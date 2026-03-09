"""Tests for test module 1887 — covers src modules [7545, 7546, 7547, 7548]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7545 import add_7545
from module_7546 import subtract_7546
from module_7547 import multiply_7547
from module_7548 import divide_7548

def test_add_7545():
    assert add_7545(2, 3) == 5

def test_subtract_7546():
    assert subtract_7546(10, 4) == 6

def test_multiply_7547():
    assert multiply_7547(3, 7) == 21

def test_divide_7548():
    assert divide_7548(10, 2) == 5.0
