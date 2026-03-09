"""Tests for test module 2343 — covers src modules [9369, 9370, 9371, 9372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9369 import add_9369
from module_9370 import subtract_9370
from module_9371 import multiply_9371
from module_9372 import divide_9372

def test_add_9369():
    assert add_9369(2, 3) == 5

def test_subtract_9370():
    assert subtract_9370(10, 4) == 6

def test_multiply_9371():
    assert multiply_9371(3, 7) == 21

def test_divide_9372():
    assert divide_9372(10, 2) == 5.0
