"""Tests for test module 2130 — covers src modules [8517, 8518, 8519, 8520]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8517 import modulo_8517
from module_8518 import power_8518
from module_8519 import min_8519
from module_8520 import max_8520

def test_modulo_8517():
    assert modulo_8517(10, 3) == 1

def test_power_8518():
    assert power_8518(2, 8) == 256

def test_min_8519():
    assert min_8519(3, 7) == 3

def test_max_8520():
    assert max_8520(3, 7) == 7
