"""Tests for test module 2180 — covers src modules [8717, 8718, 8719, 8720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8717 import modulo_8717
from module_8718 import power_8718
from module_8719 import min_8719
from module_8720 import max_8720

def test_modulo_8717():
    assert modulo_8717(10, 3) == 1

def test_power_8718():
    assert power_8718(2, 8) == 256

def test_min_8719():
    assert min_8719(3, 7) == 3

def test_max_8720():
    assert max_8720(3, 7) == 7
