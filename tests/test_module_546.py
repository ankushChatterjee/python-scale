"""Tests for test module 546 — covers src modules [2181, 2182, 2183, 2184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2181 import modulo_2181
from module_2182 import power_2182
from module_2183 import min_2183
from module_2184 import max_2184

def test_modulo_2181():
    assert modulo_2181(10, 3) == 1

def test_power_2182():
    assert power_2182(2, 8) == 256

def test_min_2183():
    assert min_2183(3, 7) == 3

def test_max_2184():
    assert max_2184(3, 7) == 7
