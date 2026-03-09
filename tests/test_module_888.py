"""Tests for test module 888 — covers src modules [3549, 3550, 3551, 3552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3549 import modulo_3549
from module_3550 import power_3550
from module_3551 import min_3551
from module_3552 import max_3552

def test_modulo_3549():
    assert modulo_3549(10, 3) == 1

def test_power_3550():
    assert power_3550(2, 8) == 256

def test_min_3551():
    assert min_3551(3, 7) == 3

def test_max_3552():
    assert max_3552(3, 7) == 7
