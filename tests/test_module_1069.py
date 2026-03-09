"""Tests for test module 1069 — covers src modules [4273, 4274, 4275, 4276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4273 import add_4273
from module_4274 import subtract_4274
from module_4275 import multiply_4275
from module_4276 import divide_4276

def test_add_4273():
    assert add_4273(2, 3) == 5

def test_subtract_4274():
    assert subtract_4274(10, 4) == 6

def test_multiply_4275():
    assert multiply_4275(3, 7) == 21

def test_divide_4276():
    assert divide_4276(10, 2) == 5.0
