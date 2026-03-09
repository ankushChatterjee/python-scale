"""Tests for test module 1568 — covers src modules [6269, 6270, 6271, 6272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6269 import modulo_6269
from module_6270 import power_6270
from module_6271 import min_6271
from module_6272 import max_6272

def test_modulo_6269():
    assert modulo_6269(10, 3) == 1

def test_power_6270():
    assert power_6270(2, 8) == 256

def test_min_6271():
    assert min_6271(3, 7) == 3

def test_max_6272():
    assert max_6272(3, 7) == 7
