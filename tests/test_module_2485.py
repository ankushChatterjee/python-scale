"""Tests for test module 2485 — covers src modules [9937, 9938, 9939, 9940]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9937 import add_9937
from module_9938 import subtract_9938
from module_9939 import multiply_9939
from module_9940 import divide_9940

def test_add_9937():
    assert add_9937(2, 3) == 5

def test_subtract_9938():
    assert subtract_9938(10, 4) == 6

def test_multiply_9939():
    assert multiply_9939(3, 7) == 21

def test_divide_9940():
    assert divide_9940(10, 2) == 5.0
