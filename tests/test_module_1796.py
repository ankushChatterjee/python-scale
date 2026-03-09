"""Tests for test module 1796 — covers src modules [7181, 7182, 7183, 7184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7181 import modulo_7181
from module_7182 import power_7182
from module_7183 import min_7183
from module_7184 import max_7184

def test_modulo_7181():
    assert modulo_7181(10, 3) == 1

def test_power_7182():
    assert power_7182(2, 8) == 256

def test_min_7183():
    assert min_7183(3, 7) == 3

def test_max_7184():
    assert max_7184(3, 7) == 7
