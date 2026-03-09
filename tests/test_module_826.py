"""Tests for test module 826 — covers src modules [3301, 3302, 3303, 3304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3301 import modulo_3301
from module_3302 import power_3302
from module_3303 import min_3303
from module_3304 import max_3304

def test_modulo_3301():
    assert modulo_3301(10, 3) == 1

def test_power_3302():
    assert power_3302(2, 8) == 256

def test_min_3303():
    assert min_3303(3, 7) == 3

def test_max_3304():
    assert max_3304(3, 7) == 7
