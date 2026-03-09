"""Tests for test module 576 — covers src modules [2301, 2302, 2303, 2304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2301 import modulo_2301
from module_2302 import power_2302
from module_2303 import min_2303
from module_2304 import max_2304

def test_modulo_2301():
    assert modulo_2301(10, 3) == 1

def test_power_2302():
    assert power_2302(2, 8) == 256

def test_min_2303():
    assert min_2303(3, 7) == 3

def test_max_2304():
    assert max_2304(3, 7) == 7
