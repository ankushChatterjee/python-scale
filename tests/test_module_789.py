"""Tests for test module 789 — covers src modules [3153, 3154, 3155, 3156]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3153 import add_3153
from module_3154 import subtract_3154
from module_3155 import multiply_3155
from module_3156 import divide_3156

def test_add_3153():
    assert add_3153(2, 3) == 5

def test_subtract_3154():
    assert subtract_3154(10, 4) == 6

def test_multiply_3155():
    assert multiply_3155(3, 7) == 21

def test_divide_3156():
    assert divide_3156(10, 2) == 5.0
