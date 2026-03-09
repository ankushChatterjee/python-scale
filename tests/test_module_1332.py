"""Tests for test module 1332 — covers src modules [5325, 5326, 5327, 5328]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5325 import modulo_5325
from module_5326 import power_5326
from module_5327 import min_5327
from module_5328 import max_5328

def test_modulo_5325():
    assert modulo_5325(10, 3) == 1

def test_power_5326():
    assert power_5326(2, 8) == 256

def test_min_5327():
    assert min_5327(3, 7) == 3

def test_max_5328():
    assert max_5328(3, 7) == 7
