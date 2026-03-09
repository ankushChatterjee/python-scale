"""Tests for test module 1680 — covers src modules [6717, 6718, 6719, 6720]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6717 import modulo_6717
from module_6718 import power_6718
from module_6719 import min_6719
from module_6720 import max_6720

def test_modulo_6717():
    assert modulo_6717(10, 3) == 1

def test_power_6718():
    assert power_6718(2, 8) == 256

def test_min_6719():
    assert min_6719(3, 7) == 3

def test_max_6720():
    assert max_6720(3, 7) == 7
