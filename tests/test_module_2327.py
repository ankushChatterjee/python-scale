"""Tests for test module 2327 — covers src modules [9305, 9306, 9307, 9308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9305 import add_9305
from module_9306 import subtract_9306
from module_9307 import multiply_9307
from module_9308 import divide_9308

def test_add_9305():
    assert add_9305(2, 3) == 5

def test_subtract_9306():
    assert subtract_9306(10, 4) == 6

def test_multiply_9307():
    assert multiply_9307(3, 7) == 21

def test_divide_9308():
    assert divide_9308(10, 2) == 5.0
