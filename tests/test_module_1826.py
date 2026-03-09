"""Tests for test module 1826 — covers src modules [7301, 7302, 7303, 7304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7301 import modulo_7301
from module_7302 import power_7302
from module_7303 import min_7303
from module_7304 import max_7304

def test_modulo_7301():
    assert modulo_7301(10, 3) == 1

def test_power_7302():
    assert power_7302(2, 8) == 256

def test_min_7303():
    assert min_7303(3, 7) == 3

def test_max_7304():
    assert max_7304(3, 7) == 7
