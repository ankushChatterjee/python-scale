"""Tests for test module 1100 — covers src modules [4397, 4398, 4399, 4400]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4397 import modulo_4397
from module_4398 import power_4398
from module_4399 import min_4399
from module_4400 import max_4400

def test_modulo_4397():
    assert modulo_4397(10, 3) == 1

def test_power_4398():
    assert power_4398(2, 8) == 256

def test_min_4399():
    assert min_4399(3, 7) == 3

def test_max_4400():
    assert max_4400(3, 7) == 7
