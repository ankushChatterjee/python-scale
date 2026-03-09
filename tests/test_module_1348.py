"""Tests for test module 1348 — covers src modules [5389, 5390, 5391, 5392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5389 import modulo_5389
from module_5390 import power_5390
from module_5391 import min_5391
from module_5392 import max_5392

def test_modulo_5389():
    assert modulo_5389(10, 3) == 1

def test_power_5390():
    assert power_5390(2, 8) == 256

def test_min_5391():
    assert min_5391(3, 7) == 3

def test_max_5392():
    assert max_5392(3, 7) == 7
