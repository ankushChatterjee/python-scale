"""Tests for test module 2188 — covers src modules [8749, 8750, 8751, 8752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8749 import modulo_8749
from module_8750 import power_8750
from module_8751 import min_8751
from module_8752 import max_8752

def test_modulo_8749():
    assert modulo_8749(10, 3) == 1

def test_power_8750():
    assert power_8750(2, 8) == 256

def test_min_8751():
    assert min_8751(3, 7) == 3

def test_max_8752():
    assert max_8752(3, 7) == 7
