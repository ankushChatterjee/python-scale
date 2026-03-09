"""Tests for test module 2291 — covers src modules [9161, 9162, 9163, 9164]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9161 import add_9161
from module_9162 import subtract_9162
from module_9163 import multiply_9163
from module_9164 import divide_9164

def test_add_9161():
    assert add_9161(2, 3) == 5

def test_subtract_9162():
    assert subtract_9162(10, 4) == 6

def test_multiply_9163():
    assert multiply_9163(3, 7) == 21

def test_divide_9164():
    assert divide_9164(10, 2) == 5.0
