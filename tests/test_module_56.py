"""Tests for test module 56 — covers src modules [221, 222, 223, 224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_221 import modulo_221
from module_222 import power_222
from module_223 import min_223
from module_224 import max_224

def test_modulo_221():
    assert modulo_221(10, 3) == 1

def test_power_222():
    assert power_222(2, 8) == 256

def test_min_223():
    assert min_223(3, 7) == 3

def test_max_224():
    assert max_224(3, 7) == 7
