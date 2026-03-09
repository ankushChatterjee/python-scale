"""Tests for test module 2326 — covers src modules [9301, 9302, 9303, 9304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9301 import modulo_9301
from module_9302 import power_9302
from module_9303 import min_9303
from module_9304 import max_9304

def test_modulo_9301():
    assert modulo_9301(10, 3) == 1

def test_power_9302():
    assert power_9302(2, 8) == 256

def test_min_9303():
    assert min_9303(3, 7) == 3

def test_max_9304():
    assert max_9304(3, 7) == 7
