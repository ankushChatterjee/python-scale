"""Tests for test module 1710 — covers src modules [6837, 6838, 6839, 6840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6837 import modulo_6837
from module_6838 import power_6838
from module_6839 import min_6839
from module_6840 import max_6840

def test_modulo_6837():
    assert modulo_6837(10, 3) == 1

def test_power_6838():
    assert power_6838(2, 8) == 256

def test_min_6839():
    assert min_6839(3, 7) == 3

def test_max_6840():
    assert max_6840(3, 7) == 7
