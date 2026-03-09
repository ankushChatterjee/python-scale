"""Tests for test module 1188 — covers src modules [4749, 4750, 4751, 4752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4749 import modulo_4749
from module_4750 import power_4750
from module_4751 import min_4751
from module_4752 import max_4752

def test_modulo_4749():
    assert modulo_4749(10, 3) == 1

def test_power_4750():
    assert power_4750(2, 8) == 256

def test_min_4751():
    assert min_4751(3, 7) == 3

def test_max_4752():
    assert max_4752(3, 7) == 7
