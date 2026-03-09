"""Tests for module 235."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_235 import max_235, divide_235, add_235, modulo_235

def test_max_235():
    assert max_235(3, 7) == 7

def test_divide_235():
    assert divide_235(10, 2) == 5.0

def test_add_235():
    assert add_235(2, 3) == 5

def test_modulo_235():
    assert modulo_235(10, 3) == 1
