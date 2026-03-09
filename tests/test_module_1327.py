"""Tests for test module 1327 — covers src modules [5305, 5306, 5307, 5308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5305 import add_5305
from module_5306 import subtract_5306
from module_5307 import multiply_5307
from module_5308 import divide_5308

def test_add_5305():
    assert add_5305(2, 3) == 5

def test_subtract_5306():
    assert subtract_5306(10, 4) == 6

def test_multiply_5307():
    assert multiply_5307(3, 7) == 21

def test_divide_5308():
    assert divide_5308(10, 2) == 5.0
