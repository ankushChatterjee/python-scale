"""Tests for test module 1076 — covers src modules [4301, 4302, 4303, 4304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4301 import modulo_4301
from module_4302 import power_4302
from module_4303 import min_4303
from module_4304 import max_4304

def test_modulo_4301():
    assert modulo_4301(10, 3) == 1

def test_power_4302():
    assert power_4302(2, 8) == 256

def test_min_4303():
    assert min_4303(3, 7) == 3

def test_max_4304():
    assert max_4304(3, 7) == 7
