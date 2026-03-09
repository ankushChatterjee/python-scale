"""Tests for test module 1072 — covers src modules [4285, 4286, 4287, 4288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4285 import modulo_4285
from module_4286 import power_4286
from module_4287 import min_4287
from module_4288 import max_4288

def test_modulo_4285():
    assert modulo_4285(10, 3) == 1

def test_power_4286():
    assert power_4286(2, 8) == 256

def test_min_4287():
    assert min_4287(3, 7) == 3

def test_max_4288():
    assert max_4288(3, 7) == 7
