"""Tests for test module 2378 — covers src modules [9509, 9510, 9511, 9512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9509 import modulo_9509
from module_9510 import power_9510
from module_9511 import min_9511
from module_9512 import max_9512

def test_modulo_9509():
    assert modulo_9509(10, 3) == 1

def test_power_9510():
    assert power_9510(2, 8) == 256

def test_min_9511():
    assert min_9511(3, 7) == 3

def test_max_9512():
    assert max_9512(3, 7) == 7
