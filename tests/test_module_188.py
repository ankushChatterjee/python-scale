"""Tests for test module 188 — covers src modules [749, 750, 751, 752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_749 import modulo_749
from module_750 import power_750
from module_751 import min_751
from module_752 import max_752

def test_modulo_749():
    assert modulo_749(10, 3) == 1

def test_power_750():
    assert power_750(2, 8) == 256

def test_min_751():
    assert min_751(3, 7) == 3

def test_max_752():
    assert max_752(3, 7) == 7
