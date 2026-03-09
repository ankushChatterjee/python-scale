"""Tests for test module 1087 — covers src modules [4345, 4346, 4347, 4348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4345 import add_4345
from module_4346 import subtract_4346
from module_4347 import multiply_4347
from module_4348 import divide_4348

def test_add_4345():
    assert add_4345(2, 3) == 5

def test_subtract_4346():
    assert subtract_4346(10, 4) == 6

def test_multiply_4347():
    assert multiply_4347(3, 7) == 21

def test_divide_4348():
    assert divide_4348(10, 2) == 5.0
