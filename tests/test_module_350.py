"""Tests for test module 350 — covers src modules [1397, 1398, 1399, 1400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1397 import modulo_1397
from module_1398 import power_1398
from module_1399 import min_1399
from module_1400 import max_1400

def test_modulo_1397():
    assert modulo_1397(10, 3) == 1

def test_power_1398():
    assert power_1398(2, 8) == 256

def test_min_1399():
    assert min_1399(3, 7) == 3

def test_max_1400():
    assert max_1400(3, 7) == 7
