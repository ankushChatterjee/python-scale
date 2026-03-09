"""Tests for test module 628 — covers src modules [2509, 2510, 2511, 2512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2509 import modulo_2509
from module_2510 import power_2510
from module_2511 import min_2511
from module_2512 import max_2512

def test_modulo_2509():
    assert modulo_2509(10, 3) == 1

def test_power_2510():
    assert power_2510(2, 8) == 256

def test_min_2511():
    assert min_2511(3, 7) == 3

def test_max_2512():
    assert max_2512(3, 7) == 7
