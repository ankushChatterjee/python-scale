"""Tests for test module 2392 — covers src modules [9565, 9566, 9567, 9568]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9565 import modulo_9565
from module_9566 import power_9566
from module_9567 import min_9567
from module_9568 import max_9568

def test_modulo_9565():
    assert modulo_9565(10, 3) == 1

def test_power_9566():
    assert power_9566(2, 8) == 256

def test_min_9567():
    assert min_9567(3, 7) == 3

def test_max_9568():
    assert max_9568(3, 7) == 7
