"""Tests for test module 2022 — covers src modules [8085, 8086, 8087, 8088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8085 import modulo_8085
from module_8086 import power_8086
from module_8087 import min_8087
from module_8088 import max_8088

def test_modulo_8085():
    assert modulo_8085(10, 3) == 1

def test_power_8086():
    assert power_8086(2, 8) == 256

def test_min_8087():
    assert min_8087(3, 7) == 3

def test_max_8088():
    assert max_8088(3, 7) == 7
