"""Tests for test module 1536 — covers src modules [6141, 6142, 6143, 6144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6141 import modulo_6141
from module_6142 import power_6142
from module_6143 import min_6143
from module_6144 import max_6144

def test_modulo_6141():
    assert modulo_6141(10, 3) == 1

def test_power_6142():
    assert power_6142(2, 8) == 256

def test_min_6143():
    assert min_6143(3, 7) == 3

def test_max_6144():
    assert max_6144(3, 7) == 7
