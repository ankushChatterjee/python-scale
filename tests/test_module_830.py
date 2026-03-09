"""Tests for test module 830 — covers src modules [3317, 3318, 3319, 3320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3317 import modulo_3317
from module_3318 import power_3318
from module_3319 import min_3319
from module_3320 import max_3320

def test_modulo_3317():
    assert modulo_3317(10, 3) == 1

def test_power_3318():
    assert power_3318(2, 8) == 256

def test_min_3319():
    assert min_3319(3, 7) == 3

def test_max_3320():
    assert max_3320(3, 7) == 7
