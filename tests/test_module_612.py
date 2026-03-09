"""Tests for test module 612 — covers src modules [2445, 2446, 2447, 2448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2445 import modulo_2445
from module_2446 import power_2446
from module_2447 import min_2447
from module_2448 import max_2448

def test_modulo_2445():
    assert modulo_2445(10, 3) == 1

def test_power_2446():
    assert power_2446(2, 8) == 256

def test_min_2447():
    assert min_2447(3, 7) == 3

def test_max_2448():
    assert max_2448(3, 7) == 7
