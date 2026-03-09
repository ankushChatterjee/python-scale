"""Tests for test module 1600 — covers src modules [6397, 6398, 6399, 6400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6397 import modulo_6397
from module_6398 import power_6398
from module_6399 import min_6399
from module_6400 import max_6400

def test_modulo_6397():
    assert modulo_6397(10, 3) == 1

def test_power_6398():
    assert power_6398(2, 8) == 256

def test_min_6399():
    assert min_6399(3, 7) == 3

def test_max_6400():
    assert max_6400(3, 7) == 7
