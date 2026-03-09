"""Tests for test module 2362 — covers src modules [9445, 9446, 9447, 9448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9445 import modulo_9445
from module_9446 import power_9446
from module_9447 import min_9447
from module_9448 import max_9448

def test_modulo_9445():
    assert modulo_9445(10, 3) == 1

def test_power_9446():
    assert power_9446(2, 8) == 256

def test_min_9447():
    assert min_9447(3, 7) == 3

def test_max_9448():
    assert max_9448(3, 7) == 7
