"""Tests for test module 2258 — covers src modules [9029, 9030, 9031, 9032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9029 import modulo_9029
from module_9030 import power_9030
from module_9031 import min_9031
from module_9032 import max_9032

def test_modulo_9029():
    assert modulo_9029(10, 3) == 1

def test_power_9030():
    assert power_9030(2, 8) == 256

def test_min_9031():
    assert min_9031(3, 7) == 3

def test_max_9032():
    assert max_9032(3, 7) == 7
