"""Tests for test module 2337 — covers src modules [9345, 9346, 9347, 9348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9345 import add_9345
from module_9346 import subtract_9346
from module_9347 import multiply_9347
from module_9348 import divide_9348

def test_add_9345():
    assert add_9345(2, 3) == 5

def test_subtract_9346():
    assert subtract_9346(10, 4) == 6

def test_multiply_9347():
    assert multiply_9347(3, 7) == 21

def test_divide_9348():
    assert divide_9348(10, 2) == 5.0
