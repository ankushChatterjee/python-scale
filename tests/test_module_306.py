"""Tests for test module 306 — covers src modules [1221, 1222, 1223, 1224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1221 import modulo_1221
from module_1222 import power_1222
from module_1223 import min_1223
from module_1224 import max_1224

def test_modulo_1221():
    assert modulo_1221(10, 3) == 1

def test_power_1222():
    assert power_1222(2, 8) == 256

def test_min_1223():
    assert min_1223(3, 7) == 3

def test_max_1224():
    assert max_1224(3, 7) == 7
