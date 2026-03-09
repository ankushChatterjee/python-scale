"""Tests for test module 1099 — covers src modules [4393, 4394, 4395, 4396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4393 import add_4393
from module_4394 import subtract_4394
from module_4395 import multiply_4395
from module_4396 import divide_4396

def test_add_4393():
    assert add_4393(2, 3) == 5

def test_subtract_4394():
    assert subtract_4394(10, 4) == 6

def test_multiply_4395():
    assert multiply_4395(3, 7) == 21

def test_divide_4396():
    assert divide_4396(10, 2) == 5.0
