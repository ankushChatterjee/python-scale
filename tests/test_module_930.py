"""Tests for test module 930 — covers src modules [3717, 3718, 3719, 3720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3717 import modulo_3717
from module_3718 import power_3718
from module_3719 import min_3719
from module_3720 import max_3720

def test_modulo_3717():
    assert modulo_3717(10, 3) == 1

def test_power_3718():
    assert power_3718(2, 8) == 256

def test_min_3719():
    assert min_3719(3, 7) == 3

def test_max_3720():
    assert max_3720(3, 7) == 7
