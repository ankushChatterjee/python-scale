"""Tests for test module 2079 — covers src modules [8313, 8314, 8315, 8316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8313 import add_8313
from module_8314 import subtract_8314
from module_8315 import multiply_8315
from module_8316 import divide_8316

def test_add_8313():
    assert add_8313(2, 3) == 5

def test_subtract_8314():
    assert subtract_8314(10, 4) == 6

def test_multiply_8315():
    assert multiply_8315(3, 7) == 21

def test_divide_8316():
    assert divide_8316(10, 2) == 5.0
