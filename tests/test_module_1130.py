"""Tests for test module 1130 — covers src modules [4517, 4518, 4519, 4520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4517 import modulo_4517
from module_4518 import power_4518
from module_4519 import min_4519
from module_4520 import max_4520

def test_modulo_4517():
    assert modulo_4517(10, 3) == 1

def test_power_4518():
    assert power_4518(2, 8) == 256

def test_min_4519():
    assert min_4519(3, 7) == 3

def test_max_4520():
    assert max_4520(3, 7) == 7
