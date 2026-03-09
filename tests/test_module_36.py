"""Tests for test module 36 — covers src modules [141, 142, 143, 144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_141 import modulo_141
from module_142 import power_142
from module_143 import min_143
from module_144 import max_144

def test_modulo_141():
    assert modulo_141(10, 3) == 1

def test_power_142():
    assert power_142(2, 8) == 256

def test_min_143():
    assert min_143(3, 7) == 3

def test_max_144():
    assert max_144(3, 7) == 7
