"""Tests for test module 2099 — covers src modules [8393, 8394, 8395, 8396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8393 import add_8393
from module_8394 import subtract_8394
from module_8395 import multiply_8395
from module_8396 import divide_8396

def test_add_8393():
    assert add_8393(2, 3) == 5

def test_subtract_8394():
    assert subtract_8394(10, 4) == 6

def test_multiply_8395():
    assert multiply_8395(3, 7) == 21

def test_divide_8396():
    assert divide_8396(10, 2) == 5.0
