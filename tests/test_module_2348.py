"""Tests for test module 2348 — covers src modules [9389, 9390, 9391, 9392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9389 import modulo_9389
from module_9390 import power_9390
from module_9391 import min_9391
from module_9392 import max_9392

def test_modulo_9389():
    assert modulo_9389(10, 3) == 1

def test_power_9390():
    assert power_9390(2, 8) == 256

def test_min_9391():
    assert min_9391(3, 7) == 3

def test_max_9392():
    assert max_9392(3, 7) == 7
