"""Tests for test module 2080 — covers src modules [8317, 8318, 8319, 8320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8317 import modulo_8317
from module_8318 import power_8318
from module_8319 import min_8319
from module_8320 import max_8320

def test_modulo_8317():
    assert modulo_8317(10, 3) == 1

def test_power_8318():
    assert power_8318(2, 8) == 256

def test_min_8319():
    assert min_8319(3, 7) == 3

def test_max_8320():
    assert max_8320(3, 7) == 7
