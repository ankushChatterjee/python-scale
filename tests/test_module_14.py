"""Tests for test module 14 — covers src modules [53, 54, 55, 56]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_53 import modulo_53
from module_54 import power_54
from module_55 import min_55
from module_56 import max_56

def test_modulo_53():
    assert modulo_53(10, 3) == 1

def test_power_54():
    assert power_54(2, 8) == 256

def test_min_55():
    assert min_55(3, 7) == 3

def test_max_56():
    assert max_56(3, 7) == 7
