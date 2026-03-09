"""Tests for test module 2134 — covers src modules [8533, 8534, 8535, 8536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8533 import modulo_8533
from module_8534 import power_8534
from module_8535 import min_8535
from module_8536 import max_8536

def test_modulo_8533():
    assert modulo_8533(10, 3) == 1

def test_power_8534():
    assert power_8534(2, 8) == 256

def test_min_8535():
    assert min_8535(3, 7) == 3

def test_max_8536():
    assert max_8536(3, 7) == 7
