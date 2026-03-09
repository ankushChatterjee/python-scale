"""Tests for test module 1350 — covers src modules [5397, 5398, 5399, 5400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5397 import modulo_5397
from module_5398 import power_5398
from module_5399 import min_5399
from module_5400 import max_5400

def test_modulo_5397():
    assert modulo_5397(10, 3) == 1

def test_power_5398():
    assert power_5398(2, 8) == 256

def test_min_5399():
    assert min_5399(3, 7) == 3

def test_max_5400():
    assert max_5400(3, 7) == 7
