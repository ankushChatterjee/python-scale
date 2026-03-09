"""Tests for test module 1322 — covers src modules [5285, 5286, 5287, 5288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5285 import modulo_5285
from module_5286 import power_5286
from module_5287 import min_5287
from module_5288 import max_5288

def test_modulo_5285():
    assert modulo_5285(10, 3) == 1

def test_power_5286():
    assert power_5286(2, 8) == 256

def test_min_5287():
    assert min_5287(3, 7) == 3

def test_max_5288():
    assert max_5288(3, 7) == 7
