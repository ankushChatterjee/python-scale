"""Tests for test module 1306 — covers src modules [5221, 5222, 5223, 5224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5221 import modulo_5221
from module_5222 import power_5222
from module_5223 import min_5223
from module_5224 import max_5224

def test_modulo_5221():
    assert modulo_5221(10, 3) == 1

def test_power_5222():
    assert power_5222(2, 8) == 256

def test_min_5223():
    assert min_5223(3, 7) == 3

def test_max_5224():
    assert max_5224(3, 7) == 7
