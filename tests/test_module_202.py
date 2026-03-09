"""Tests for test module 202 — covers src modules [805, 806, 807, 808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_805 import modulo_805
from module_806 import power_806
from module_807 import min_807
from module_808 import max_808

def test_modulo_805():
    assert modulo_805(10, 3) == 1

def test_power_806():
    assert power_806(2, 8) == 256

def test_min_807():
    assert min_807(3, 7) == 3

def test_max_808():
    assert max_808(3, 7) == 7
