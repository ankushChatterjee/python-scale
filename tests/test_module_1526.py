"""Tests for test module 1526 — covers src modules [6101, 6102, 6103, 6104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6101 import modulo_6101
from module_6102 import power_6102
from module_6103 import min_6103
from module_6104 import max_6104

def test_modulo_6101():
    assert modulo_6101(10, 3) == 1

def test_power_6102():
    assert power_6102(2, 8) == 256

def test_min_6103():
    assert min_6103(3, 7) == 3

def test_max_6104():
    assert max_6104(3, 7) == 7
