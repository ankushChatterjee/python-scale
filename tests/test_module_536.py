"""Tests for test module 536 — covers src modules [2141, 2142, 2143, 2144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2141 import modulo_2141
from module_2142 import power_2142
from module_2143 import min_2143
from module_2144 import max_2144

def test_modulo_2141():
    assert modulo_2141(10, 3) == 1

def test_power_2142():
    assert power_2142(2, 8) == 256

def test_min_2143():
    assert min_2143(3, 7) == 3

def test_max_2144():
    assert max_2144(3, 7) == 7
