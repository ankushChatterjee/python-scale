"""Tests for test module 1344 — covers src modules [5373, 5374, 5375, 5376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5373 import modulo_5373
from module_5374 import power_5374
from module_5375 import min_5375
from module_5376 import max_5376

def test_modulo_5373():
    assert modulo_5373(10, 3) == 1

def test_power_5374():
    assert power_5374(2, 8) == 256

def test_min_5375():
    assert min_5375(3, 7) == 3

def test_max_5376():
    assert max_5376(3, 7) == 7
