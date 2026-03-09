"""Tests for test module 638 — covers src modules [2549, 2550, 2551, 2552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2549 import modulo_2549
from module_2550 import power_2550
from module_2551 import min_2551
from module_2552 import max_2552

def test_modulo_2549():
    assert modulo_2549(10, 3) == 1

def test_power_2550():
    assert power_2550(2, 8) == 256

def test_min_2551():
    assert min_2551(3, 7) == 3

def test_max_2552():
    assert max_2552(3, 7) == 7
