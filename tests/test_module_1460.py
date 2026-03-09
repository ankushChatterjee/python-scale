"""Tests for test module 1460 — covers src modules [5837, 5838, 5839, 5840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5837 import modulo_5837
from module_5838 import power_5838
from module_5839 import min_5839
from module_5840 import max_5840

def test_modulo_5837():
    assert modulo_5837(10, 3) == 1

def test_power_5838():
    assert power_5838(2, 8) == 256

def test_min_5839():
    assert min_5839(3, 7) == 3

def test_max_5840():
    assert max_5840(3, 7) == 7
