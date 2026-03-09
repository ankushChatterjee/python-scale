"""Tests for test module 174 — covers src modules [693, 694, 695, 696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_693 import modulo_693
from module_694 import power_694
from module_695 import min_695
from module_696 import max_696

def test_modulo_693():
    assert modulo_693(10, 3) == 1

def test_power_694():
    assert power_694(2, 8) == 256

def test_min_695():
    assert min_695(3, 7) == 3

def test_max_696():
    assert max_696(3, 7) == 7
