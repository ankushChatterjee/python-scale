"""Tests for test module 26 — covers src modules [101, 102, 103, 104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_101 import modulo_101
from module_102 import power_102
from module_103 import min_103
from module_104 import max_104

def test_modulo_101():
    assert modulo_101(10, 3) == 1

def test_power_102():
    assert power_102(2, 8) == 256

def test_min_103():
    assert min_103(3, 7) == 3

def test_max_104():
    assert max_104(3, 7) == 7
