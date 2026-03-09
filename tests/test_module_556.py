"""Tests for test module 556 — covers src modules [2221, 2222, 2223, 2224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2221 import modulo_2221
from module_2222 import power_2222
from module_2223 import min_2223
from module_2224 import max_2224

def test_modulo_2221():
    assert modulo_2221(10, 3) == 1

def test_power_2222():
    assert power_2222(2, 8) == 256

def test_min_2223():
    assert min_2223(3, 7) == 3

def test_max_2224():
    assert max_2224(3, 7) == 7
