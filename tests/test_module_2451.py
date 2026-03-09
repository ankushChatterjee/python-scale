"""Tests for test module 2451 — covers src modules [9801, 9802, 9803, 9804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9801 import add_9801
from module_9802 import subtract_9802
from module_9803 import multiply_9803
from module_9804 import divide_9804

def test_add_9801():
    assert add_9801(2, 3) == 5

def test_subtract_9802():
    assert subtract_9802(10, 4) == 6

def test_multiply_9803():
    assert multiply_9803(3, 7) == 21

def test_divide_9804():
    assert divide_9804(10, 2) == 5.0
