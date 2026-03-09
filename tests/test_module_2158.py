"""Tests for test module 2158 — covers src modules [8629, 8630, 8631, 8632]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8629 import modulo_8629
from module_8630 import power_8630
from module_8631 import min_8631
from module_8632 import max_8632

def test_modulo_8629():
    assert modulo_8629(10, 3) == 1

def test_power_8630():
    assert power_8630(2, 8) == 256

def test_min_8631():
    assert min_8631(3, 7) == 3

def test_max_8632():
    assert max_8632(3, 7) == 7
