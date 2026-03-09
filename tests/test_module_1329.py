"""Tests for test module 1329 — covers src modules [5313, 5314, 5315, 5316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5313 import add_5313
from module_5314 import subtract_5314
from module_5315 import multiply_5315
from module_5316 import divide_5316

def test_add_5313():
    assert add_5313(2, 3) == 5

def test_subtract_5314():
    assert subtract_5314(10, 4) == 6

def test_multiply_5315():
    assert multiply_5315(3, 7) == 21

def test_divide_5316():
    assert divide_5316(10, 2) == 5.0
