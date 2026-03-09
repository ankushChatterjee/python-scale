"""Tests for test module 1068 — covers src modules [4269, 4270, 4271, 4272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4269 import modulo_4269
from module_4270 import power_4270
from module_4271 import min_4271
from module_4272 import max_4272

def test_modulo_4269():
    assert modulo_4269(10, 3) == 1

def test_power_4270():
    assert power_4270(2, 8) == 256

def test_min_4271():
    assert min_4271(3, 7) == 3

def test_max_4272():
    assert max_4272(3, 7) == 7
