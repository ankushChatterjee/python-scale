"""Tests for test module 680 — covers src modules [2717, 2718, 2719, 2720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2717 import modulo_2717
from module_2718 import power_2718
from module_2719 import min_2719
from module_2720 import max_2720

def test_modulo_2717():
    assert modulo_2717(10, 3) == 1

def test_power_2718():
    assert power_2718(2, 8) == 256

def test_min_2719():
    assert min_2719(3, 7) == 3

def test_max_2720():
    assert max_2720(3, 7) == 7
