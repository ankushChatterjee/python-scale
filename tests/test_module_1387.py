"""Tests for test module 1387 — covers src modules [5545, 5546, 5547, 5548]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5545 import add_5545
from module_5546 import subtract_5546
from module_5547 import multiply_5547
from module_5548 import divide_5548

def test_add_5545():
    assert add_5545(2, 3) == 5

def test_subtract_5546():
    assert subtract_5546(10, 4) == 6

def test_multiply_5547():
    assert multiply_5547(3, 7) == 21

def test_divide_5548():
    assert divide_5548(10, 2) == 5.0
