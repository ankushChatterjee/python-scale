"""Tests for test module 1829 — covers src modules [7313, 7314, 7315, 7316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7313 import add_7313
from module_7314 import subtract_7314
from module_7315 import multiply_7315
from module_7316 import divide_7316

def test_add_7313():
    assert add_7313(2, 3) == 5

def test_subtract_7314():
    assert subtract_7314(10, 4) == 6

def test_multiply_7315():
    assert multiply_7315(3, 7) == 21

def test_divide_7316():
    assert divide_7316(10, 2) == 5.0
