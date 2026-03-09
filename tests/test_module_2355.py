"""Tests for test module 2355 — covers src modules [9417, 9418, 9419, 9420]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9417 import add_9417
from module_9418 import subtract_9418
from module_9419 import multiply_9419
from module_9420 import divide_9420

def test_add_9417():
    assert add_9417(2, 3) == 5

def test_subtract_9418():
    assert subtract_9418(10, 4) == 6

def test_multiply_9419():
    assert multiply_9419(3, 7) == 21

def test_divide_9420():
    assert divide_9420(10, 2) == 5.0
