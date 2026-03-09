"""Tests for test module 1408 — covers src modules [5629, 5630, 5631, 5632]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5629 import modulo_5629
from module_5630 import power_5630
from module_5631 import min_5631
from module_5632 import max_5632

def test_modulo_5629():
    assert modulo_5629(10, 3) == 1

def test_power_5630():
    assert power_5630(2, 8) == 256

def test_min_5631():
    assert min_5631(3, 7) == 3

def test_max_5632():
    assert max_5632(3, 7) == 7
