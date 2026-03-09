"""Tests for test module 1805 — covers src modules [7217, 7218, 7219, 7220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7217 import add_7217
from module_7218 import subtract_7218
from module_7219 import multiply_7219
from module_7220 import divide_7220

def test_add_7217():
    assert add_7217(2, 3) == 5

def test_subtract_7218():
    assert subtract_7218(10, 4) == 6

def test_multiply_7219():
    assert multiply_7219(3, 7) == 21

def test_divide_7220():
    assert divide_7220(10, 2) == 5.0
