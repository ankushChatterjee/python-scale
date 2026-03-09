"""Tests for test module 2329 — covers src modules [9313, 9314, 9315, 9316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9313 import add_9313
from module_9314 import subtract_9314
from module_9315 import multiply_9315
from module_9316 import divide_9316

def test_add_9313():
    assert add_9313(2, 3) == 5

def test_subtract_9314():
    assert subtract_9314(10, 4) == 6

def test_multiply_9315():
    assert multiply_9315(3, 7) == 21

def test_divide_9316():
    assert divide_9316(10, 2) == 5.0
