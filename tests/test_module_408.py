"""Tests for test module 408 — covers src modules [1629, 1630, 1631, 1632]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1629 import modulo_1629
from module_1630 import power_1630
from module_1631 import min_1631
from module_1632 import max_1632

def test_modulo_1629():
    assert modulo_1629(10, 3) == 1

def test_power_1630():
    assert power_1630(2, 8) == 256

def test_min_1631():
    assert min_1631(3, 7) == 3

def test_max_1632():
    assert max_1632(3, 7) == 7
