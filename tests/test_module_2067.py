"""Tests for test module 2067 — covers src modules [8265, 8266, 8267, 8268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8265 import add_8265
from module_8266 import subtract_8266
from module_8267 import multiply_8267
from module_8268 import divide_8268

def test_add_8265():
    assert add_8265(2, 3) == 5

def test_subtract_8266():
    assert subtract_8266(10, 4) == 6

def test_multiply_8267():
    assert multiply_8267(3, 7) == 21

def test_divide_8268():
    assert divide_8268(10, 2) == 5.0
