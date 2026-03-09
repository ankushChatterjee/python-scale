"""Tests for test module 1664 — covers src modules [6653, 6654, 6655, 6656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6653 import modulo_6653
from module_6654 import power_6654
from module_6655 import min_6655
from module_6656 import max_6656

def test_modulo_6653():
    assert modulo_6653(10, 3) == 1

def test_power_6654():
    assert power_6654(2, 8) == 256

def test_min_6655():
    assert min_6655(3, 7) == 3

def test_max_6656():
    assert max_6656(3, 7) == 7
