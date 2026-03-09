"""Tests for test module 564 — covers src modules [2253, 2254, 2255, 2256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2253 import modulo_2253
from module_2254 import power_2254
from module_2255 import min_2255
from module_2256 import max_2256

def test_modulo_2253():
    assert modulo_2253(10, 3) == 1

def test_power_2254():
    assert power_2254(2, 8) == 256

def test_min_2255():
    assert min_2255(3, 7) == 3

def test_max_2256():
    assert max_2256(3, 7) == 7
