"""Tests for test module 2153 — covers src modules [8609, 8610, 8611, 8612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8609 import add_8609
from module_8610 import subtract_8610
from module_8611 import multiply_8611
from module_8612 import divide_8612

def test_add_8609():
    assert add_8609(2, 3) == 5

def test_subtract_8610():
    assert subtract_8610(10, 4) == 6

def test_multiply_8611():
    assert multiply_8611(3, 7) == 21

def test_divide_8612():
    assert divide_8612(10, 2) == 5.0
