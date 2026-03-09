"""Tests for test module 849 — covers src modules [3393, 3394, 3395, 3396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3393 import add_3393
from module_3394 import subtract_3394
from module_3395 import multiply_3395
from module_3396 import divide_3396

def test_add_3393():
    assert add_3393(2, 3) == 5

def test_subtract_3394():
    assert subtract_3394(10, 4) == 6

def test_multiply_3395():
    assert multiply_3395(3, 7) == 21

def test_divide_3396():
    assert divide_3396(10, 2) == 5.0
