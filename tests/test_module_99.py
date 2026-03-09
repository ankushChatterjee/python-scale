"""Tests for test module 99 — covers src modules [393, 394, 395, 396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_393 import add_393
from module_394 import subtract_394
from module_395 import multiply_395
from module_396 import divide_396

def test_add_393():
    assert add_393(2, 3) == 5

def test_subtract_394():
    assert subtract_394(10, 4) == 6

def test_multiply_395():
    assert multiply_395(3, 7) == 21

def test_divide_396():
    assert divide_396(10, 2) == 5.0
