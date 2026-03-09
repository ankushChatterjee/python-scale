"""Tests for test module 820 — covers src modules [3277, 3278, 3279, 3280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3277 import modulo_3277
from module_3278 import power_3278
from module_3279 import min_3279
from module_3280 import max_3280

def test_modulo_3277():
    assert modulo_3277(10, 3) == 1

def test_power_3278():
    assert power_3278(2, 8) == 256

def test_min_3279():
    assert min_3279(3, 7) == 3

def test_max_3280():
    assert max_3280(3, 7) == 7
