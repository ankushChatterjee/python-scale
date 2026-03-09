"""Tests for test module 2388 — covers src modules [9549, 9550, 9551, 9552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9549 import modulo_9549
from module_9550 import power_9550
from module_9551 import min_9551
from module_9552 import max_9552

def test_modulo_9549():
    assert modulo_9549(10, 3) == 1

def test_power_9550():
    assert power_9550(2, 8) == 256

def test_min_9551():
    assert min_9551(3, 7) == 3

def test_max_9552():
    assert max_9552(3, 7) == 7
