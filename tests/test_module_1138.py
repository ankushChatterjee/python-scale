"""Tests for test module 1138 — covers src modules [4549, 4550, 4551, 4552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4549 import modulo_4549
from module_4550 import power_4550
from module_4551 import min_4551
from module_4552 import max_4552

def test_modulo_4549():
    assert modulo_4549(10, 3) == 1

def test_power_4550():
    assert power_4550(2, 8) == 256

def test_min_4551():
    assert min_4551(3, 7) == 3

def test_max_4552():
    assert max_4552(3, 7) == 7
