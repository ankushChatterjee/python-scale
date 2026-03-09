"""Tests for test module 100 — covers src modules [397, 398, 399, 400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_397 import modulo_397
from module_398 import power_398
from module_399 import min_399
from module_400 import max_400

def test_modulo_397():
    assert modulo_397(10, 3) == 1

def test_power_398():
    assert power_398(2, 8) == 256

def test_min_399():
    assert min_399(3, 7) == 3

def test_max_400():
    assert max_400(3, 7) == 7
