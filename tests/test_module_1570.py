"""Tests for test module 1570 — covers src modules [6277, 6278, 6279, 6280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6277 import modulo_6277
from module_6278 import power_6278
from module_6279 import min_6279
from module_6280 import max_6280

def test_modulo_6277():
    assert modulo_6277(10, 3) == 1

def test_power_6278():
    assert power_6278(2, 8) == 256

def test_min_6279():
    assert min_6279(3, 7) == 3

def test_max_6280():
    assert max_6280(3, 7) == 7
