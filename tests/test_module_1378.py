"""Tests for test module 1378 — covers src modules [5509, 5510, 5511, 5512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5509 import modulo_5509
from module_5510 import power_5510
from module_5511 import min_5511
from module_5512 import max_5512

def test_modulo_5509():
    assert modulo_5509(10, 3) == 1

def test_power_5510():
    assert power_5510(2, 8) == 256

def test_min_5511():
    assert min_5511(3, 7) == 3

def test_max_5512():
    assert max_5512(3, 7) == 7
