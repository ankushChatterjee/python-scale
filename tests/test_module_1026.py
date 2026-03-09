"""Tests for test module 1026 — covers src modules [4101, 4102, 4103, 4104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4101 import modulo_4101
from module_4102 import power_4102
from module_4103 import min_4103
from module_4104 import max_4104

def test_modulo_4101():
    assert modulo_4101(10, 3) == 1

def test_power_4102():
    assert power_4102(2, 8) == 256

def test_min_4103():
    assert min_4103(3, 7) == 3

def test_max_4104():
    assert max_4104(3, 7) == 7
