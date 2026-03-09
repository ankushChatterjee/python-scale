"""Tests for test module 1079 — covers src modules [4313, 4314, 4315, 4316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4313 import add_4313
from module_4314 import subtract_4314
from module_4315 import multiply_4315
from module_4316 import divide_4316

def test_add_4313():
    assert add_4313(2, 3) == 5

def test_subtract_4314():
    assert subtract_4314(10, 4) == 6

def test_multiply_4315():
    assert multiply_4315(3, 7) == 21

def test_divide_4316():
    assert divide_4316(10, 2) == 5.0
