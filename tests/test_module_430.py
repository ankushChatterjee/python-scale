"""Tests for test module 430 — covers src modules [1717, 1718, 1719, 1720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1717 import modulo_1717
from module_1718 import power_1718
from module_1719 import min_1719
from module_1720 import max_1720

def test_modulo_1717():
    assert modulo_1717(10, 3) == 1

def test_power_1718():
    assert power_1718(2, 8) == 256

def test_min_1719():
    assert min_1719(3, 7) == 3

def test_max_1720():
    assert max_1720(3, 7) == 7
