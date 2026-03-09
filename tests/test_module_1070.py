"""Tests for test module 1070 — covers src modules [4277, 4278, 4279, 4280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4277 import modulo_4277
from module_4278 import power_4278
from module_4279 import min_4279
from module_4280 import max_4280

def test_modulo_4277():
    assert modulo_4277(10, 3) == 1

def test_power_4278():
    assert power_4278(2, 8) == 256

def test_min_4279():
    assert min_4279(3, 7) == 3

def test_max_4280():
    assert max_4280(3, 7) == 7
