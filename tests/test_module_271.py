"""Tests for test module 271 — covers src modules [1081, 1082, 1083, 1084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1081 import add_1081
from module_1082 import subtract_1082
from module_1083 import multiply_1083
from module_1084 import divide_1084

def test_add_1081():
    assert add_1081(2, 3) == 5

def test_subtract_1082():
    assert subtract_1082(10, 4) == 6

def test_multiply_1083():
    assert multiply_1083(3, 7) == 21

def test_divide_1084():
    assert divide_1084(10, 2) == 5.0
