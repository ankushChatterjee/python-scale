"""Tests for test module 1176 — covers src modules [4701, 4702, 4703, 4704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4701 import modulo_4701
from module_4702 import power_4702
from module_4703 import min_4703
from module_4704 import max_4704

def test_modulo_4701():
    assert modulo_4701(10, 3) == 1

def test_power_4702():
    assert power_4702(2, 8) == 256

def test_min_4703():
    assert min_4703(3, 7) == 3

def test_max_4704():
    assert max_4704(3, 7) == 7
