"""Tests for test module 2064 — covers src modules [8253, 8254, 8255, 8256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8253 import modulo_8253
from module_8254 import power_8254
from module_8255 import min_8255
from module_8256 import max_8256

def test_modulo_8253():
    assert modulo_8253(10, 3) == 1

def test_power_8254():
    assert power_8254(2, 8) == 256

def test_min_8255():
    assert min_8255(3, 7) == 3

def test_max_8256():
    assert max_8256(3, 7) == 7
