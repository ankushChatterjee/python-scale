"""Tests for test module 2070 — covers src modules [8277, 8278, 8279, 8280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8277 import modulo_8277
from module_8278 import power_8278
from module_8279 import min_8279
from module_8280 import max_8280

def test_modulo_8277():
    assert modulo_8277(10, 3) == 1

def test_power_8278():
    assert power_8278(2, 8) == 256

def test_min_8279():
    assert min_8279(3, 7) == 3

def test_max_8280():
    assert max_8280(3, 7) == 7
