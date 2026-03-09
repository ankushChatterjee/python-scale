"""Tests for test module 326 — covers src modules [1301, 1302, 1303, 1304]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1301 import modulo_1301
from module_1302 import power_1302
from module_1303 import min_1303
from module_1304 import max_1304

def test_modulo_1301():
    assert modulo_1301(10, 3) == 1

def test_power_1302():
    assert power_1302(2, 8) == 256

def test_min_1303():
    assert min_1303(3, 7) == 3

def test_max_1304():
    assert max_1304(3, 7) == 7
