"""Tests for test module 344 — covers src modules [1373, 1374, 1375, 1376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1373 import modulo_1373
from module_1374 import power_1374
from module_1375 import min_1375
from module_1376 import max_1376

def test_modulo_1373():
    assert modulo_1373(10, 3) == 1

def test_power_1374():
    assert power_1374(2, 8) == 256

def test_min_1375():
    assert min_1375(3, 7) == 3

def test_max_1376():
    assert max_1376(3, 7) == 7
