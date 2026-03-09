"""Tests for test module 584 — covers src modules [2333, 2334, 2335, 2336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2333 import modulo_2333
from module_2334 import power_2334
from module_2335 import min_2335
from module_2336 import max_2336

def test_modulo_2333():
    assert modulo_2333(10, 3) == 1

def test_power_2334():
    assert power_2334(2, 8) == 256

def test_min_2335():
    assert min_2335(3, 7) == 3

def test_max_2336():
    assert max_2336(3, 7) == 7
