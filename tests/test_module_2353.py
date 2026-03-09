"""Tests for test module 2353 — covers src modules [9409, 9410, 9411, 9412]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9409 import add_9409
from module_9410 import subtract_9410
from module_9411 import multiply_9411
from module_9412 import divide_9412

def test_add_9409():
    assert add_9409(2, 3) == 5

def test_subtract_9410():
    assert subtract_9410(10, 4) == 6

def test_multiply_9411():
    assert multiply_9411(3, 7) == 21

def test_divide_9412():
    assert divide_9412(10, 2) == 5.0
