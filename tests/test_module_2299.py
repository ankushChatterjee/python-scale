"""Tests for test module 2299 — covers src modules [9193, 9194, 9195, 9196]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9193 import add_9193
from module_9194 import subtract_9194
from module_9195 import multiply_9195
from module_9196 import divide_9196

def test_add_9193():
    assert add_9193(2, 3) == 5

def test_subtract_9194():
    assert subtract_9194(10, 4) == 6

def test_multiply_9195():
    assert multiply_9195(3, 7) == 21

def test_divide_9196():
    assert divide_9196(10, 2) == 5.0
