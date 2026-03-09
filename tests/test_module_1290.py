"""Tests for test module 1290 — covers src modules [5157, 5158, 5159, 5160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5157 import modulo_5157
from module_5158 import power_5158
from module_5159 import min_5159
from module_5160 import max_5160

def test_modulo_5157():
    assert modulo_5157(10, 3) == 1

def test_power_5158():
    assert power_5158(2, 8) == 256

def test_min_5159():
    assert min_5159(3, 7) == 3

def test_max_5160():
    assert max_5160(3, 7) == 7
