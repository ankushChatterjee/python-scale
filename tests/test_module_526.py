"""Tests for test module 526 — covers src modules [2101, 2102, 2103, 2104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2101 import modulo_2101
from module_2102 import power_2102
from module_2103 import min_2103
from module_2104 import max_2104

def test_modulo_2101():
    assert modulo_2101(10, 3) == 1

def test_power_2102():
    assert power_2102(2, 8) == 256

def test_min_2103():
    assert min_2103(3, 7) == 3

def test_max_2104():
    assert max_2104(3, 7) == 7
