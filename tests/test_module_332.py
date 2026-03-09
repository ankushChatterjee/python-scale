"""Tests for test module 332 — covers src modules [1325, 1326, 1327, 1328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1325 import modulo_1325
from module_1326 import power_1326
from module_1327 import min_1327
from module_1328 import max_1328

def test_modulo_1325():
    assert modulo_1325(10, 3) == 1

def test_power_1326():
    assert power_1326(2, 8) == 256

def test_min_1327():
    assert min_1327(3, 7) == 3

def test_max_1328():
    assert max_1328(3, 7) == 7
