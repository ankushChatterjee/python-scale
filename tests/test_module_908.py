"""Tests for test module 908 — covers src modules [3629, 3630, 3631, 3632]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3629 import modulo_3629
from module_3630 import power_3630
from module_3631 import min_3631
from module_3632 import max_3632

def test_modulo_3629():
    assert modulo_3629(10, 3) == 1

def test_power_3630():
    assert power_3630(2, 8) == 256

def test_min_3631():
    assert min_3631(3, 7) == 3

def test_max_3632():
    assert max_3632(3, 7) == 7
