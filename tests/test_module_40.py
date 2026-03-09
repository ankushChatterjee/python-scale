"""Tests for test module 40 — covers src modules [157, 158, 159, 160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_157 import modulo_157
from module_158 import power_158
from module_159 import min_159
from module_160 import max_160

def test_modulo_157():
    assert modulo_157(10, 3) == 1

def test_power_158():
    assert power_158(2, 8) == 256

def test_min_159():
    assert min_159(3, 7) == 3

def test_max_160():
    assert max_160(3, 7) == 7
