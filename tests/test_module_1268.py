"""Tests for test module 1268 — covers src modules [5069, 5070, 5071, 5072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5069 import modulo_5069
from module_5070 import power_5070
from module_5071 import min_5071
from module_5072 import max_5072

def test_modulo_5069():
    assert modulo_5069(10, 3) == 1

def test_power_5070():
    assert power_5070(2, 8) == 256

def test_min_5071():
    assert min_5071(3, 7) == 3

def test_max_5072():
    assert max_5072(3, 7) == 7
