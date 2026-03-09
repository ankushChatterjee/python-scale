"""Tests for test module 2026 — covers src modules [8101, 8102, 8103, 8104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8101 import modulo_8101
from module_8102 import power_8102
from module_8103 import min_8103
from module_8104 import max_8104

def test_modulo_8101():
    assert modulo_8101(10, 3) == 1

def test_power_8102():
    assert power_8102(2, 8) == 256

def test_min_8103():
    assert min_8103(3, 7) == 3

def test_max_8104():
    assert max_8104(3, 7) == 7
