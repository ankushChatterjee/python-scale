"""Tests for test module 1832 — covers src modules [7325, 7326, 7327, 7328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7325 import modulo_7325
from module_7326 import power_7326
from module_7327 import min_7327
from module_7328 import max_7328

def test_modulo_7325():
    assert modulo_7325(10, 3) == 1

def test_power_7326():
    assert power_7326(2, 8) == 256

def test_min_7327():
    assert min_7327(3, 7) == 3

def test_max_7328():
    assert max_7328(3, 7) == 7
