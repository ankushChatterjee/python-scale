"""Tests for test module 771 — covers src modules [3081, 3082, 3083, 3084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3081 import add_3081
from module_3082 import subtract_3082
from module_3083 import multiply_3083
from module_3084 import divide_3084

def test_add_3081():
    assert add_3081(2, 3) == 5

def test_subtract_3082():
    assert subtract_3082(10, 4) == 6

def test_multiply_3083():
    assert multiply_3083(3, 7) == 21

def test_divide_3084():
    assert divide_3084(10, 2) == 5.0
