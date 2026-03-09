"""Tests for test module 1556 — covers src modules [6221, 6222, 6223, 6224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6221 import modulo_6221
from module_6222 import power_6222
from module_6223 import min_6223
from module_6224 import max_6224

def test_modulo_6221():
    assert modulo_6221(10, 3) == 1

def test_power_6222():
    assert power_6222(2, 8) == 256

def test_min_6223():
    assert min_6223(3, 7) == 3

def test_max_6224():
    assert max_6224(3, 7) == 7
