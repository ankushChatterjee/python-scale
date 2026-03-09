"""Tests for test module 818 — covers src modules [3269, 3270, 3271, 3272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3269 import modulo_3269
from module_3270 import power_3270
from module_3271 import min_3271
from module_3272 import max_3272

def test_modulo_3269():
    assert modulo_3269(10, 3) == 1

def test_power_3270():
    assert power_3270(2, 8) == 256

def test_min_3271():
    assert min_3271(3, 7) == 3

def test_max_3272():
    assert max_3272(3, 7) == 7
