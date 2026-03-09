"""Tests for module 219."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_219 import max_219, divide_219, multiply_219, modulo_219

def test_max_219():
    assert max_219(3, 7) == 7

def test_divide_219():
    assert divide_219(10, 2) == 5.0

def test_multiply_219():
    assert multiply_219(3, 7) == 21

def test_modulo_219():
    assert modulo_219(10, 3) == 1
