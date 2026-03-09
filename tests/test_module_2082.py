"""Tests for test module 2082 — covers src modules [8325, 8326, 8327, 8328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8325 import modulo_8325
from module_8326 import power_8326
from module_8327 import min_8327
from module_8328 import max_8328

def test_modulo_8325():
    assert modulo_8325(10, 3) == 1

def test_power_8326():
    assert power_8326(2, 8) == 256

def test_min_8327():
    assert min_8327(3, 7) == 3

def test_max_8328():
    assert max_8328(3, 7) == 7
