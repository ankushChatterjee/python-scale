"""Tests for test module 1772 — covers src modules [7085, 7086, 7087, 7088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7085 import modulo_7085
from module_7086 import power_7086
from module_7087 import min_7087
from module_7088 import max_7088

def test_modulo_7085():
    assert modulo_7085(10, 3) == 1

def test_power_7086():
    assert power_7086(2, 8) == 256

def test_min_7087():
    assert min_7087(3, 7) == 3

def test_max_7088():
    assert max_7088(3, 7) == 7
