"""Tests for test module 2401 — covers src modules [9601, 9602, 9603, 9604]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9601 import add_9601
from module_9602 import subtract_9602
from module_9603 import multiply_9603
from module_9604 import divide_9604

def test_add_9601():
    assert add_9601(2, 3) == 5

def test_subtract_9602():
    assert subtract_9602(10, 4) == 6

def test_multiply_9603():
    assert multiply_9603(3, 7) == 21

def test_divide_9604():
    assert divide_9604(10, 2) == 5.0
