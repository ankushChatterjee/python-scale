"""Tests for test module 1430 — covers src modules [5717, 5718, 5719, 5720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5717 import modulo_5717
from module_5718 import power_5718
from module_5719 import min_5719
from module_5720 import max_5720

def test_modulo_5717():
    assert modulo_5717(10, 3) == 1

def test_power_5718():
    assert power_5718(2, 8) == 256

def test_min_5719():
    assert min_5719(3, 7) == 3

def test_max_5720():
    assert max_5720(3, 7) == 7
