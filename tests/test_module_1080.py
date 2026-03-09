"""Tests for test module 1080 — covers src modules [4317, 4318, 4319, 4320]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4317 import modulo_4317
from module_4318 import power_4318
from module_4319 import min_4319
from module_4320 import max_4320

def test_modulo_4317():
    assert modulo_4317(10, 3) == 1

def test_power_4318():
    assert power_4318(2, 8) == 256

def test_min_4319():
    assert min_4319(3, 7) == 3

def test_max_4320():
    assert max_4320(3, 7) == 7
