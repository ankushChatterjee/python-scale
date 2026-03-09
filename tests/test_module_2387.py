"""Tests for test module 2387 — covers src modules [9545, 9546, 9547, 9548]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9545 import add_9545
from module_9546 import subtract_9546
from module_9547 import multiply_9547
from module_9548 import divide_9548

def test_add_9545():
    assert add_9545(2, 3) == 5

def test_subtract_9546():
    assert subtract_9546(10, 4) == 6

def test_multiply_9547():
    assert multiply_9547(3, 7) == 21

def test_divide_9548():
    assert divide_9548(10, 2) == 5.0
