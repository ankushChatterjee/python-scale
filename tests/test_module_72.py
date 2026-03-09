"""Tests for test module 72 — covers src modules [285, 286, 287, 288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_285 import modulo_285
from module_286 import power_286
from module_287 import min_287
from module_288 import max_288

def test_modulo_285():
    assert modulo_285(10, 3) == 1

def test_power_286():
    assert power_286(2, 8) == 256

def test_min_287():
    assert min_287(3, 7) == 3

def test_max_288():
    assert max_288(3, 7) == 7
