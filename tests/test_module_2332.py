"""Tests for test module 2332 — covers src modules [9325, 9326, 9327, 9328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9325 import modulo_9325
from module_9326 import power_9326
from module_9327 import min_9327
from module_9328 import max_9328

def test_modulo_9325():
    assert modulo_9325(10, 3) == 1

def test_power_9326():
    assert power_9326(2, 8) == 256

def test_min_9327():
    assert min_9327(3, 7) == 3

def test_max_9328():
    assert max_9328(3, 7) == 7
