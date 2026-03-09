"""Tests for test module 1112 — covers src modules [4445, 4446, 4447, 4448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4445 import modulo_4445
from module_4446 import power_4446
from module_4447 import min_4447
from module_4448 import max_4448

def test_modulo_4445():
    assert modulo_4445(10, 3) == 1

def test_power_4446():
    assert power_4446(2, 8) == 256

def test_min_4447():
    assert min_4447(3, 7) == 3

def test_max_4448():
    assert max_4448(3, 7) == 7
