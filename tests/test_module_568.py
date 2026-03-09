"""Tests for test module 568 — covers src modules [2269, 2270, 2271, 2272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2269 import modulo_2269
from module_2270 import power_2270
from module_2271 import min_2271
from module_2272 import max_2272

def test_modulo_2269():
    assert modulo_2269(10, 3) == 1

def test_power_2270():
    assert power_2270(2, 8) == 256

def test_min_2271():
    assert min_2271(3, 7) == 3

def test_max_2272():
    assert max_2272(3, 7) == 7
