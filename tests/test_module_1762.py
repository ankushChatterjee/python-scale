"""Tests for test module 1762 — covers src modules [7045, 7046, 7047, 7048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7045 import modulo_7045
from module_7046 import power_7046
from module_7047 import min_7047
from module_7048 import max_7048

def test_modulo_7045():
    assert modulo_7045(10, 3) == 1

def test_power_7046():
    assert power_7046(2, 8) == 256

def test_min_7047():
    assert min_7047(3, 7) == 3

def test_max_7048():
    assert max_7048(3, 7) == 7
