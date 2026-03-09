"""Tests for test module 76 — covers src modules [301, 302, 303, 304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_301 import modulo_301
from module_302 import power_302
from module_303 import min_303
from module_304 import max_304

def test_modulo_301():
    assert modulo_301(10, 3) == 1

def test_power_302():
    assert power_302(2, 8) == 256

def test_min_303():
    assert min_303(3, 7) == 3

def test_max_304():
    assert max_304(3, 7) == 7
