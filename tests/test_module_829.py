"""Tests for test module 829 — covers src modules [3313, 3314, 3315, 3316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3313 import add_3313
from module_3314 import subtract_3314
from module_3315 import multiply_3315
from module_3316 import divide_3316

def test_add_3313():
    assert add_3313(2, 3) == 5

def test_subtract_3314():
    assert subtract_3314(10, 4) == 6

def test_multiply_3315():
    assert multiply_3315(3, 7) == 21

def test_divide_3316():
    assert divide_3316(10, 2) == 5.0
