"""Tests for test module 1326 — covers src modules [5301, 5302, 5303, 5304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5301 import modulo_5301
from module_5302 import power_5302
from module_5303 import min_5303
from module_5304 import max_5304

def test_modulo_5301():
    assert modulo_5301(10, 3) == 1

def test_power_5302():
    assert power_5302(2, 8) == 256

def test_min_5303():
    assert min_5303(3, 7) == 3

def test_max_5304():
    assert max_5304(3, 7) == 7
