"""Tests for test module 878 — covers src modules [3509, 3510, 3511, 3512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3509 import modulo_3509
from module_3510 import power_3510
from module_3511 import min_3511
from module_3512 import max_3512

def test_modulo_3509():
    assert modulo_3509(10, 3) == 1

def test_power_3510():
    assert power_3510(2, 8) == 256

def test_min_3511():
    assert min_3511(3, 7) == 3

def test_max_3512():
    assert max_3512(3, 7) == 7
