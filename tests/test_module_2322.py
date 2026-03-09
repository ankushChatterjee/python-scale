"""Tests for test module 2322 — covers src modules [9285, 9286, 9287, 9288]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9285 import modulo_9285
from module_9286 import power_9286
from module_9287 import min_9287
from module_9288 import max_9288

def test_modulo_9285():
    assert modulo_9285(10, 3) == 1

def test_power_9286():
    assert power_9286(2, 8) == 256

def test_min_9287():
    assert min_9287(3, 7) == 3

def test_max_9288():
    assert max_9288(3, 7) == 7
