"""Tests for test module 329 — covers src modules [1313, 1314, 1315, 1316]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1313 import add_1313
from module_1314 import subtract_1314
from module_1315 import multiply_1315
from module_1316 import divide_1316

def test_add_1313():
    assert add_1313(2, 3) == 5

def test_subtract_1314():
    assert subtract_1314(10, 4) == 6

def test_multiply_1315():
    assert multiply_1315(3, 7) == 21

def test_divide_1316():
    assert divide_1316(10, 2) == 5.0
