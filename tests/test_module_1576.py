"""Tests for test module 1576 — covers src modules [6301, 6302, 6303, 6304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6301 import modulo_6301
from module_6302 import power_6302
from module_6303 import min_6303
from module_6304 import max_6304

def test_modulo_6301():
    assert modulo_6301(10, 3) == 1

def test_power_6302():
    assert power_6302(2, 8) == 256

def test_min_6303():
    assert min_6303(3, 7) == 3

def test_max_6304():
    assert max_6304(3, 7) == 7
