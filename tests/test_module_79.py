"""Tests for test module 79 — covers src modules [313, 314, 315, 316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_313 import add_313
from module_314 import subtract_314
from module_315 import multiply_315
from module_316 import divide_316

def test_add_313():
    assert add_313(2, 3) == 5

def test_subtract_314():
    assert subtract_314(10, 4) == 6

def test_multiply_315():
    assert multiply_315(3, 7) == 21

def test_divide_316():
    assert divide_316(10, 2) == 5.0
