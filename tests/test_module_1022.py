"""Tests for test module 1022 — covers src modules [4085, 4086, 4087, 4088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4085 import modulo_4085
from module_4086 import power_4086
from module_4087 import min_4087
from module_4088 import max_4088

def test_modulo_4085():
    assert modulo_4085(10, 3) == 1

def test_power_4086():
    assert power_4086(2, 8) == 256

def test_min_4087():
    assert min_4087(3, 7) == 3

def test_max_4088():
    assert max_4088(3, 7) == 7
