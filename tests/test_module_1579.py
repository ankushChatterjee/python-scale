"""Tests for test module 1579 — covers src modules [6313, 6314, 6315, 6316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6313 import add_6313
from module_6314 import subtract_6314
from module_6315 import multiply_6315
from module_6316 import divide_6316

def test_add_6313():
    assert add_6313(2, 3) == 5

def test_subtract_6314():
    assert subtract_6314(10, 4) == 6

def test_multiply_6315():
    assert multiply_6315(3, 7) == 21

def test_divide_6316():
    assert divide_6316(10, 2) == 5.0
