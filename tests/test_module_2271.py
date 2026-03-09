"""Tests for test module 2271 — covers src modules [9081, 9082, 9083, 9084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9081 import add_9081
from module_9082 import subtract_9082
from module_9083 import multiply_9083
from module_9084 import divide_9084

def test_add_9081():
    assert add_9081(2, 3) == 5

def test_subtract_9082():
    assert subtract_9082(10, 4) == 6

def test_multiply_9083():
    assert multiply_9083(3, 7) == 21

def test_divide_9084():
    assert divide_9084(10, 2) == 5.0
