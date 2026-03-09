"""Tests for test module 2100 — covers src modules [8397, 8398, 8399, 8400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8397 import modulo_8397
from module_8398 import power_8398
from module_8399 import min_8399
from module_8400 import max_8400

def test_modulo_8397():
    assert modulo_8397(10, 3) == 1

def test_power_8398():
    assert power_8398(2, 8) == 256

def test_min_8399():
    assert min_8399(3, 7) == 3

def test_max_8400():
    assert max_8400(3, 7) == 7
