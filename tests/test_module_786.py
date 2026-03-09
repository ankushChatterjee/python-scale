"""Tests for test module 786 — covers src modules [3141, 3142, 3143, 3144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3141 import modulo_3141
from module_3142 import power_3142
from module_3143 import min_3143
from module_3144 import max_3144

def test_modulo_3141():
    assert modulo_3141(10, 3) == 1

def test_power_3142():
    assert power_3142(2, 8) == 256

def test_min_3143():
    assert min_3143(3, 7) == 3

def test_max_3144():
    assert max_3144(3, 7) == 7
