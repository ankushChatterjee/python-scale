"""Tests for test module 1914 — covers src modules [7653, 7654, 7655, 7656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7653 import modulo_7653
from module_7654 import power_7654
from module_7655 import min_7655
from module_7656 import max_7656

def test_modulo_7653():
    assert modulo_7653(10, 3) == 1

def test_power_7654():
    assert power_7654(2, 8) == 256

def test_min_7655():
    assert min_7655(3, 7) == 3

def test_max_7656():
    assert max_7656(3, 7) == 7
