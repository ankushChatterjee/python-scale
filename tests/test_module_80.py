"""Tests for test module 80 — covers src modules [317, 318, 319, 320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_317 import modulo_317
from module_318 import power_318
from module_319 import min_319
from module_320 import max_320

def test_modulo_317():
    assert modulo_317(10, 3) == 1

def test_power_318():
    assert power_318(2, 8) == 256

def test_min_319():
    assert min_319(3, 7) == 3

def test_max_320():
    assert max_320(3, 7) == 7
