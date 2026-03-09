"""Tests for test module 1776 — covers src modules [7101, 7102, 7103, 7104]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7101 import modulo_7101
from module_7102 import power_7102
from module_7103 import min_7103
from module_7104 import max_7104

def test_modulo_7101():
    assert modulo_7101(10, 3) == 1

def test_power_7102():
    assert power_7102(2, 8) == 256

def test_min_7103():
    assert min_7103(3, 7) == 3

def test_max_7104():
    assert max_7104(3, 7) == 7
