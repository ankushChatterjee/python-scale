"""Tests for test module 2257 — covers src modules [9025, 9026, 9027, 9028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9025 import add_9025
from module_9026 import subtract_9026
from module_9027 import multiply_9027
from module_9028 import divide_9028

def test_add_9025():
    assert add_9025(2, 3) == 5

def test_subtract_9026():
    assert subtract_9026(10, 4) == 6

def test_multiply_9027():
    assert multiply_9027(3, 7) == 21

def test_divide_9028():
    assert divide_9028(10, 2) == 5.0
