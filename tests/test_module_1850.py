"""Tests for test module 1850 — covers src modules [7397, 7398, 7399, 7400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7397 import modulo_7397
from module_7398 import power_7398
from module_7399 import min_7399
from module_7400 import max_7400

def test_modulo_7397():
    assert modulo_7397(10, 3) == 1

def test_power_7398():
    assert power_7398(2, 8) == 256

def test_min_7399():
    assert min_7399(3, 7) == 3

def test_max_7400():
    assert max_7400(3, 7) == 7
