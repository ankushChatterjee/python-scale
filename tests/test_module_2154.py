"""Tests for test module 2154 — covers src modules [8613, 8614, 8615, 8616]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8613 import modulo_8613
from module_8614 import power_8614
from module_8615 import min_8615
from module_8616 import max_8616

def test_modulo_8613():
    assert modulo_8613(10, 3) == 1

def test_power_8614():
    assert power_8614(2, 8) == 256

def test_min_8615():
    assert min_8615(3, 7) == 3

def test_max_8616():
    assert max_8616(3, 7) == 7
