"""Tests for test module 210 — covers src modules [837, 838, 839, 840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_837 import modulo_837
from module_838 import power_838
from module_839 import min_839
from module_840 import max_840

def test_modulo_837():
    assert modulo_837(10, 3) == 1

def test_power_838():
    assert power_838(2, 8) == 256

def test_min_839():
    assert min_839(3, 7) == 3

def test_max_840():
    assert max_840(3, 7) == 7
