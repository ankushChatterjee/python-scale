"""Tests for test module 1930 — covers src modules [7717, 7718, 7719, 7720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7717 import modulo_7717
from module_7718 import power_7718
from module_7719 import min_7719
from module_7720 import max_7720

def test_modulo_7717():
    assert modulo_7717(10, 3) == 1

def test_power_7718():
    assert power_7718(2, 8) == 256

def test_min_7719():
    assert min_7719(3, 7) == 3

def test_max_7720():
    assert max_7720(3, 7) == 7
