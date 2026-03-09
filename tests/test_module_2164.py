"""Tests for test module 2164 — covers src modules [8653, 8654, 8655, 8656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8653 import modulo_8653
from module_8654 import power_8654
from module_8655 import min_8655
from module_8656 import max_8656

def test_modulo_8653():
    assert modulo_8653(10, 3) == 1

def test_power_8654():
    assert power_8654(2, 8) == 256

def test_min_8655():
    assert min_8655(3, 7) == 3

def test_max_8656():
    assert max_8656(3, 7) == 7
