"""Tests for test module 2321 — covers src modules [9281, 9282, 9283, 9284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9281 import add_9281
from module_9282 import subtract_9282
from module_9283 import multiply_9283
from module_9284 import divide_9284

def test_add_9281():
    assert add_9281(2, 3) == 5

def test_subtract_9282():
    assert subtract_9282(10, 4) == 6

def test_multiply_9283():
    assert multiply_9283(3, 7) == 21

def test_divide_9284():
    assert divide_9284(10, 2) == 5.0
