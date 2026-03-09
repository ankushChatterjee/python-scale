"""Tests for test module 2030 — covers src modules [8117, 8118, 8119, 8120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8117 import modulo_8117
from module_8118 import power_8118
from module_8119 import min_8119
from module_8120 import max_8120

def test_modulo_8117():
    assert modulo_8117(10, 3) == 1

def test_power_8118():
    assert power_8118(2, 8) == 256

def test_min_8119():
    assert min_8119(3, 7) == 3

def test_max_8120():
    assert max_8120(3, 7) == 7
