"""Tests for test module 2376 — covers src modules [9501, 9502, 9503, 9504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9501 import modulo_9501
from module_9502 import power_9502
from module_9503 import min_9503
from module_9504 import max_9504

def test_modulo_9501():
    assert modulo_9501(10, 3) == 1

def test_power_9502():
    assert power_9502(2, 8) == 256

def test_min_9503():
    assert min_9503(3, 7) == 3

def test_max_9504():
    assert max_9504(3, 7) == 7
