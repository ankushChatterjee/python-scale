"""Tests for test module 320 — covers src modules [1277, 1278, 1279, 1280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1277 import modulo_1277
from module_1278 import power_1278
from module_1279 import min_1279
from module_1280 import max_1280

def test_modulo_1277():
    assert modulo_1277(10, 3) == 1

def test_power_1278():
    assert power_1278(2, 8) == 256

def test_min_1279():
    assert min_1279(3, 7) == 3

def test_max_1280():
    assert max_1280(3, 7) == 7
