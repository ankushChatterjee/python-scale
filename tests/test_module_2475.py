"""Tests for test module 2475 — covers src modules [9897, 9898, 9899, 9900]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9897 import add_9897
from module_9898 import subtract_9898
from module_9899 import multiply_9899
from module_9900 import divide_9900

def test_add_9897():
    assert add_9897(2, 3) == 5

def test_subtract_9898():
    assert subtract_9898(10, 4) == 6

def test_multiply_9899():
    assert multiply_9899(3, 7) == 21

def test_divide_9900():
    assert divide_9900(10, 2) == 5.0
