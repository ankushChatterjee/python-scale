"""Tests for test module 10 — covers src modules [37, 38, 39, 40]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_37 import modulo_37
from module_38 import power_38
from module_39 import min_39
from module_40 import max_40

def test_modulo_37():
    assert modulo_37(10, 3) == 1

def test_power_38():
    assert power_38(2, 8) == 256

def test_min_39():
    assert min_39(3, 7) == 3

def test_max_40():
    assert max_40(3, 7) == 7
