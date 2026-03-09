"""Tests for test module 1056 — covers src modules [4221, 4222, 4223, 4224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4221 import modulo_4221
from module_4222 import power_4222
from module_4223 import min_4223
from module_4224 import max_4224

def test_modulo_4221():
    assert modulo_4221(10, 3) == 1

def test_power_4222():
    assert power_4222(2, 8) == 256

def test_min_4223():
    assert min_4223(3, 7) == 3

def test_max_4224():
    assert max_4224(3, 7) == 7
