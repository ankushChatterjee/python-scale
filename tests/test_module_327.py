"""Tests for test module 327 — covers src modules [1305, 1306, 1307, 1308]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1305 import add_1305
from module_1306 import subtract_1306
from module_1307 import multiply_1307
from module_1308 import divide_1308

def test_add_1305():
    assert add_1305(2, 3) == 5

def test_subtract_1306():
    assert subtract_1306(10, 4) == 6

def test_multiply_1307():
    assert multiply_1307(3, 7) == 21

def test_divide_1308():
    assert divide_1308(10, 2) == 5.0
