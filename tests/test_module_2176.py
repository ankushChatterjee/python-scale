"""Tests for test module 2176 — covers src modules [8701, 8702, 8703, 8704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8701 import modulo_8701
from module_8702 import power_8702
from module_8703 import min_8703
from module_8704 import max_8704

def test_modulo_8701():
    assert modulo_8701(10, 3) == 1

def test_power_8702():
    assert power_8702(2, 8) == 256

def test_min_8703():
    assert min_8703(3, 7) == 3

def test_max_8704():
    assert max_8704(3, 7) == 7
