"""Tests for test module 378 — covers src modules [1509, 1510, 1511, 1512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1509 import modulo_1509
from module_1510 import power_1510
from module_1511 import min_1511
from module_1512 import max_1512

def test_modulo_1509():
    assert modulo_1509(10, 3) == 1

def test_power_1510():
    assert power_1510(2, 8) == 256

def test_min_1511():
    assert min_1511(3, 7) == 3

def test_max_1512():
    assert max_1512(3, 7) == 7
