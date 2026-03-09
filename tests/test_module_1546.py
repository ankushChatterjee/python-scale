"""Tests for test module 1546 — covers src modules [6181, 6182, 6183, 6184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6181 import modulo_6181
from module_6182 import power_6182
from module_6183 import min_6183
from module_6184 import max_6184

def test_modulo_6181():
    assert modulo_6181(10, 3) == 1

def test_power_6182():
    assert power_6182(2, 8) == 256

def test_min_6183():
    assert min_6183(3, 7) == 3

def test_max_6184():
    assert max_6184(3, 7) == 7
