"""Tests for test module 2331 — covers src modules [9321, 9322, 9323, 9324]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9321 import add_9321
from module_9322 import subtract_9322
from module_9323 import multiply_9323
from module_9324 import divide_9324

def test_add_9321():
    assert add_9321(2, 3) == 5

def test_subtract_9322():
    assert subtract_9322(10, 4) == 6

def test_multiply_9323():
    assert multiply_9323(3, 7) == 21

def test_divide_9324():
    assert divide_9324(10, 2) == 5.0
