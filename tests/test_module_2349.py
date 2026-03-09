"""Tests for test module 2349 — covers src modules [9393, 9394, 9395, 9396]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9393 import add_9393
from module_9394 import subtract_9394
from module_9395 import multiply_9395
from module_9396 import divide_9396

def test_add_9393():
    assert add_9393(2, 3) == 5

def test_subtract_9394():
    assert subtract_9394(10, 4) == 6

def test_multiply_9395():
    assert multiply_9395(3, 7) == 21

def test_divide_9396():
    assert divide_9396(10, 2) == 5.0
