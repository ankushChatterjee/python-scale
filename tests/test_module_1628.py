"""Tests for test module 1628 — covers src modules [6509, 6510, 6511, 6512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6509 import modulo_6509
from module_6510 import power_6510
from module_6511 import min_6511
from module_6512 import max_6512

def test_modulo_6509():
    assert modulo_6509(10, 3) == 1

def test_power_6510():
    assert power_6510(2, 8) == 256

def test_min_6511():
    assert min_6511(3, 7) == 3

def test_max_6512():
    assert max_6512(3, 7) == 7
