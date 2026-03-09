"""Tests for test module 1582 — covers src modules [6325, 6326, 6327, 6328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6325 import modulo_6325
from module_6326 import power_6326
from module_6327 import min_6327
from module_6328 import max_6328

def test_modulo_6325():
    assert modulo_6325(10, 3) == 1

def test_power_6326():
    assert power_6326(2, 8) == 256

def test_min_6327():
    assert min_6327(3, 7) == 3

def test_max_6328():
    assert max_6328(3, 7) == 7
