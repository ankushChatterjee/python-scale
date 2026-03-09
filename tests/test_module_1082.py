"""Tests for test module 1082 — covers src modules [4325, 4326, 4327, 4328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4325 import modulo_4325
from module_4326 import power_4326
from module_4327 import min_4327
from module_4328 import max_4328

def test_modulo_4325():
    assert modulo_4325(10, 3) == 1

def test_power_4326():
    assert power_4326(2, 8) == 256

def test_min_4327():
    assert min_4327(3, 7) == 3

def test_max_4328():
    assert max_4328(3, 7) == 7
