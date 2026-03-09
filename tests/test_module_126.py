"""Tests for module 126."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_126 import multiply_126, modulo_126, min_126, max_126

def test_multiply_126():
    assert multiply_126(3, 7) == 21

def test_modulo_126():
    assert modulo_126(10, 3) == 1

def test_min_126():
    assert min_126(3, 7) == 3

def test_max_126():
    assert max_126(3, 7) == 7
