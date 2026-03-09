"""Tests for test module 82 — covers src modules [325, 326, 327, 328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_325 import modulo_325
from module_326 import power_326
from module_327 import min_327
from module_328 import max_328

def test_modulo_325():
    assert modulo_325(10, 3) == 1

def test_power_326():
    assert power_326(2, 8) == 256

def test_min_327():
    assert min_327(3, 7) == 3

def test_max_328():
    assert max_328(3, 7) == 7
