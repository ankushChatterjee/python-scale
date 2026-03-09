"""Tests for test module 68 — covers src modules [269, 270, 271, 272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_269 import modulo_269
from module_270 import power_270
from module_271 import min_271
from module_272 import max_272

def test_modulo_269():
    assert modulo_269(10, 3) == 1

def test_power_270():
    assert power_270(2, 8) == 256

def test_min_271():
    assert min_271(3, 7) == 3

def test_max_272():
    assert max_272(3, 7) == 7
