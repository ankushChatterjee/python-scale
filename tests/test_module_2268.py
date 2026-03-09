"""Tests for test module 2268 — covers src modules [9069, 9070, 9071, 9072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9069 import modulo_9069
from module_9070 import power_9070
from module_9071 import min_9071
from module_9072 import max_9072

def test_modulo_9069():
    assert modulo_9069(10, 3) == 1

def test_power_9070():
    assert power_9070(2, 8) == 256

def test_min_9071():
    assert min_9071(3, 7) == 3

def test_max_9072():
    assert max_9072(3, 7) == 7
