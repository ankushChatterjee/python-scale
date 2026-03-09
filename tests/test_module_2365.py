"""Tests for test module 2365 — covers src modules [9457, 9458, 9459, 9460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9457 import add_9457
from module_9458 import subtract_9458
from module_9459 import multiply_9459
from module_9460 import divide_9460

def test_add_9457():
    assert add_9457(2, 3) == 5

def test_subtract_9458():
    assert subtract_9458(10, 4) == 6

def test_multiply_9459():
    assert multiply_9459(3, 7) == 21

def test_divide_9460():
    assert divide_9460(10, 2) == 5.0
