"""Tests for test module 1888 — covers src modules [7549, 7550, 7551, 7552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7549 import modulo_7549
from module_7550 import power_7550
from module_7551 import min_7551
from module_7552 import max_7552

def test_modulo_7549():
    assert modulo_7549(10, 3) == 1

def test_power_7550():
    assert power_7550(2, 8) == 256

def test_min_7551():
    assert min_7551(3, 7) == 3

def test_max_7552():
    assert max_7552(3, 7) == 7
