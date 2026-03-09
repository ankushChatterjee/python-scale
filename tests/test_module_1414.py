"""Tests for test module 1414 — covers src modules [5653, 5654, 5655, 5656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5653 import modulo_5653
from module_5654 import power_5654
from module_5655 import min_5655
from module_5656 import max_5656

def test_modulo_5653():
    assert modulo_5653(10, 3) == 1

def test_power_5654():
    assert power_5654(2, 8) == 256

def test_min_5655():
    assert min_5655(3, 7) == 3

def test_max_5656():
    assert max_5656(3, 7) == 7
