"""Tests for test module 77 — covers src modules [305, 306, 307, 308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_305 import add_305
from module_306 import subtract_306
from module_307 import multiply_307
from module_308 import divide_308

def test_add_305():
    assert add_305(2, 3) == 5

def test_subtract_306():
    assert subtract_306(10, 4) == 6

def test_multiply_307():
    assert multiply_307(3, 7) == 21

def test_divide_308():
    assert divide_308(10, 2) == 5.0
