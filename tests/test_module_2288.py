"""Tests for test module 2288 — covers src modules [9149, 9150, 9151, 9152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9149 import modulo_9149
from module_9150 import power_9150
from module_9151 import min_9151
from module_9152 import max_9152

def test_modulo_9149():
    assert modulo_9149(10, 3) == 1

def test_power_9150():
    assert power_9150(2, 8) == 256

def test_min_9151():
    assert min_9151(3, 7) == 3

def test_max_9152():
    assert max_9152(3, 7) == 7
