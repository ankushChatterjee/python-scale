"""Tests for test module 1276 — covers src modules [5101, 5102, 5103, 5104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5101 import modulo_5101
from module_5102 import power_5102
from module_5103 import min_5103
from module_5104 import max_5104

def test_modulo_5101():
    assert modulo_5101(10, 3) == 1

def test_power_5102():
    assert power_5102(2, 8) == 256

def test_min_5103():
    assert min_5103(3, 7) == 3

def test_max_5104():
    assert max_5104(3, 7) == 7
