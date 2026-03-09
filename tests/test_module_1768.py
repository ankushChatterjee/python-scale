"""Tests for test module 1768 — covers src modules [7069, 7070, 7071, 7072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7069 import modulo_7069
from module_7070 import power_7070
from module_7071 import min_7071
from module_7072 import max_7072

def test_modulo_7069():
    assert modulo_7069(10, 3) == 1

def test_power_7070():
    assert power_7070(2, 8) == 256

def test_min_7071():
    assert min_7071(3, 7) == 3

def test_max_7072():
    assert max_7072(3, 7) == 7
