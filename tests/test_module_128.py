"""Tests for test module 128 — covers src modules [509, 510, 511, 512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_509 import modulo_509
from module_510 import power_510
from module_511 import min_511
from module_512 import max_512

def test_modulo_509():
    assert modulo_509(10, 3) == 1

def test_power_510():
    assert power_510(2, 8) == 256

def test_min_511():
    assert min_511(3, 7) == 3

def test_max_512():
    assert max_512(3, 7) == 7
