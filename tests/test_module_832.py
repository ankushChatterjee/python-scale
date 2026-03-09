"""Tests for test module 832 — covers src modules [3325, 3326, 3327, 3328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3325 import modulo_3325
from module_3326 import power_3326
from module_3327 import min_3327
from module_3328 import max_3328

def test_modulo_3325():
    assert modulo_3325(10, 3) == 1

def test_power_3326():
    assert power_3326(2, 8) == 256

def test_min_3327():
    assert min_3327(3, 7) == 3

def test_max_3328():
    assert max_3328(3, 7) == 7
