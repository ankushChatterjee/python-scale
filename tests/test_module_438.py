"""Tests for test module 438 — covers src modules [1749, 1750, 1751, 1752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1749 import modulo_1749
from module_1750 import power_1750
from module_1751 import min_1751
from module_1752 import max_1752

def test_modulo_1749():
    assert modulo_1749(10, 3) == 1

def test_power_1750():
    assert power_1750(2, 8) == 256

def test_min_1751():
    assert min_1751(3, 7) == 3

def test_max_1752():
    assert max_1752(3, 7) == 7
