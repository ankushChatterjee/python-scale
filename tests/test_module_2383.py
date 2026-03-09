"""Tests for test module 2383 — covers src modules [9529, 9530, 9531, 9532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9529 import add_9529
from module_9530 import subtract_9530
from module_9531 import multiply_9531
from module_9532 import divide_9532

def test_add_9529():
    assert add_9529(2, 3) == 5

def test_subtract_9530():
    assert subtract_9530(10, 4) == 6

def test_multiply_9531():
    assert multiply_9531(3, 7) == 21

def test_divide_9532():
    assert divide_9532(10, 2) == 5.0
