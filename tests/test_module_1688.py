"""Tests for test module 1688 — covers src modules [6749, 6750, 6751, 6752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6749 import modulo_6749
from module_6750 import power_6750
from module_6751 import min_6751
from module_6752 import max_6752

def test_modulo_6749():
    assert modulo_6749(10, 3) == 1

def test_power_6750():
    assert power_6750(2, 8) == 256

def test_min_6751():
    assert min_6751(3, 7) == 3

def test_max_6752():
    assert max_6752(3, 7) == 7
