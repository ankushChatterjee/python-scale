"""Tests for test module 2056 — covers src modules [8221, 8222, 8223, 8224]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8221 import modulo_8221
from module_8222 import power_8222
from module_8223 import min_8223
from module_8224 import max_8224

def test_modulo_8221():
    assert modulo_8221(10, 3) == 1

def test_power_8222():
    assert power_8222(2, 8) == 256

def test_min_8223():
    assert min_8223(3, 7) == 3

def test_max_8224():
    assert max_8224(3, 7) == 7
