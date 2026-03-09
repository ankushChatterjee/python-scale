"""Tests for test module 1271 — covers src modules [5081, 5082, 5083, 5084]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5081 import add_5081
from module_5082 import subtract_5082
from module_5083 import multiply_5083
from module_5084 import divide_5084

def test_add_5081():
    assert add_5081(2, 3) == 5

def test_subtract_5082():
    assert subtract_5082(10, 4) == 6

def test_multiply_5083():
    assert multiply_5083(3, 7) == 21

def test_divide_5084():
    assert divide_5084(10, 2) == 5.0
