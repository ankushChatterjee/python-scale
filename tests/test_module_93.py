"""Tests for test module 93 — covers src modules [369, 370, 371, 372]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_369 import add_369
from module_370 import subtract_370
from module_371 import multiply_371
from module_372 import divide_372

def test_add_369():
    assert add_369(2, 3) == 5

def test_subtract_370():
    assert subtract_370(10, 4) == 6

def test_multiply_371():
    assert multiply_371(3, 7) == 21

def test_divide_372():
    assert divide_372(10, 2) == 5.0
