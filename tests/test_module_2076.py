"""Tests for test module 2076 — covers src modules [8301, 8302, 8303, 8304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8301 import modulo_8301
from module_8302 import power_8302
from module_8303 import min_8303
from module_8304 import max_8304

def test_modulo_8301():
    assert modulo_8301(10, 3) == 1

def test_power_8302():
    assert power_8302(2, 8) == 256

def test_min_8303():
    assert min_8303(3, 7) == 3

def test_max_8304():
    assert max_8304(3, 7) == 7
