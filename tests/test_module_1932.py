"""Tests for test module 1932 — covers src modules [7725, 7726, 7727, 7728]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7725 import modulo_7725
from module_7726 import power_7726
from module_7727 import min_7727
from module_7728 import max_7728

def test_modulo_7725():
    assert modulo_7725(10, 3) == 1

def test_power_7726():
    assert power_7726(2, 8) == 256

def test_min_7727():
    assert min_7727(3, 7) == 3

def test_max_7728():
    assert max_7728(3, 7) == 7
