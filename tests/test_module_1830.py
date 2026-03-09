"""Tests for test module 1830 — covers src modules [7317, 7318, 7319, 7320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7317 import modulo_7317
from module_7318 import power_7318
from module_7319 import min_7319
from module_7320 import max_7320

def test_modulo_7317():
    assert modulo_7317(10, 3) == 1

def test_power_7318():
    assert power_7318(2, 8) == 256

def test_min_7319():
    assert min_7319(3, 7) == 3

def test_max_7320():
    assert max_7320(3, 7) == 7
