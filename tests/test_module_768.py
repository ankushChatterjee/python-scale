"""Tests for test module 768 — covers src modules [3069, 3070, 3071, 3072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3069 import modulo_3069
from module_3070 import power_3070
from module_3071 import min_3071
from module_3072 import max_3072

def test_modulo_3069():
    assert modulo_3069(10, 3) == 1

def test_power_3070():
    assert power_3070(2, 8) == 256

def test_min_3071():
    assert min_3071(3, 7) == 3

def test_max_3072():
    assert max_3072(3, 7) == 7
