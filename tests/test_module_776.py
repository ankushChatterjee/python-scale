"""Tests for test module 776 — covers src modules [3101, 3102, 3103, 3104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3101 import modulo_3101
from module_3102 import power_3102
from module_3103 import min_3103
from module_3104 import max_3104

def test_modulo_3101():
    assert modulo_3101(10, 3) == 1

def test_power_3102():
    assert power_3102(2, 8) == 256

def test_min_3103():
    assert min_3103(3, 7) == 3

def test_max_3104():
    assert max_3104(3, 7) == 7
