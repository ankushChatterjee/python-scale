"""Tests for test module 2314 — covers src modules [9253, 9254, 9255, 9256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9253 import modulo_9253
from module_9254 import power_9254
from module_9255 import min_9255
from module_9256 import max_9256

def test_modulo_9253():
    assert modulo_9253(10, 3) == 1

def test_power_9254():
    assert power_9254(2, 8) == 256

def test_min_9255():
    assert min_9255(3, 7) == 3

def test_max_9256():
    assert max_9256(3, 7) == 7
