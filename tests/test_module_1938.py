"""Tests for test module 1938 — covers src modules [7749, 7750, 7751, 7752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7749 import modulo_7749
from module_7750 import power_7750
from module_7751 import min_7751
from module_7752 import max_7752

def test_modulo_7749():
    assert modulo_7749(10, 3) == 1

def test_power_7750():
    assert power_7750(2, 8) == 256

def test_min_7751():
    assert min_7751(3, 7) == 3

def test_max_7752():
    assert max_7752(3, 7) == 7
