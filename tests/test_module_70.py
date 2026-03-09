"""Tests for test module 70 — covers src modules [277, 278, 279, 280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_277 import modulo_277
from module_278 import power_278
from module_279 import min_279
from module_280 import max_280

def test_modulo_277():
    assert modulo_277(10, 3) == 1

def test_power_278():
    assert power_278(2, 8) == 256

def test_min_279():
    assert min_279(3, 7) == 3

def test_max_280():
    assert max_280(3, 7) == 7
