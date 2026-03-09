"""Tests for test module 582 — covers src modules [2325, 2326, 2327, 2328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2325 import modulo_2325
from module_2326 import power_2326
from module_2327 import min_2327
from module_2328 import max_2328

def test_modulo_2325():
    assert modulo_2325(10, 3) == 1

def test_power_2326():
    assert power_2326(2, 8) == 256

def test_min_2327():
    assert min_2327(3, 7) == 3

def test_max_2328():
    assert max_2328(3, 7) == 7
