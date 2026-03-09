"""Tests for test module 276 — covers src modules [1101, 1102, 1103, 1104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1101 import modulo_1101
from module_1102 import power_1102
from module_1103 import min_1103
from module_1104 import max_1104

def test_modulo_1101():
    assert modulo_1101(10, 3) == 1

def test_power_1102():
    assert power_1102(2, 8) == 256

def test_min_1103():
    assert min_1103(3, 7) == 3

def test_max_1104():
    assert max_1104(3, 7) == 7
