"""Tests for test module 138 — covers src modules [549, 550, 551, 552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_549 import modulo_549
from module_550 import power_550
from module_551 import min_551
from module_552 import max_552

def test_modulo_549():
    assert modulo_549(10, 3) == 1

def test_power_550():
    assert power_550(2, 8) == 256

def test_min_551():
    assert min_551(3, 7) == 3

def test_max_552():
    assert max_552(3, 7) == 7
