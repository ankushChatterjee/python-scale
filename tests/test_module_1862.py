"""Tests for test module 1862 — covers src modules [7445, 7446, 7447, 7448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7445 import modulo_7445
from module_7446 import power_7446
from module_7447 import min_7447
from module_7448 import max_7448

def test_modulo_7445():
    assert modulo_7445(10, 3) == 1

def test_power_7446():
    assert power_7446(2, 8) == 256

def test_min_7447():
    assert min_7447(3, 7) == 3

def test_max_7448():
    assert max_7448(3, 7) == 7
