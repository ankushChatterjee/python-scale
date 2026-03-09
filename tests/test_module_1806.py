"""Tests for test module 1806 — covers src modules [7221, 7222, 7223, 7224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7221 import modulo_7221
from module_7222 import power_7222
from module_7223 import min_7223
from module_7224 import max_7224

def test_modulo_7221():
    assert modulo_7221(10, 3) == 1

def test_power_7222():
    assert power_7222(2, 8) == 256

def test_min_7223():
    assert min_7223(3, 7) == 3

def test_max_7224():
    assert max_7224(3, 7) == 7
