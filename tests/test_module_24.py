"""Tests for test module 24 — covers src modules [93, 94, 95, 96]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_93 import modulo_93
from module_94 import power_94
from module_95 import min_95
from module_96 import max_96

def test_modulo_93():
    assert modulo_93(10, 3) == 1

def test_power_94():
    assert power_94(2, 8) == 256

def test_min_95():
    assert min_95(3, 7) == 3

def test_max_96():
    assert max_96(3, 7) == 7
