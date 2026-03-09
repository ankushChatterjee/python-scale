"""Tests for test module 200 — covers src modules [797, 798, 799, 800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_797 import modulo_797
from module_798 import power_798
from module_799 import min_799
from module_800 import max_800

def test_modulo_797():
    assert modulo_797(10, 3) == 1

def test_power_798():
    assert power_798(2, 8) == 256

def test_min_799():
    assert min_799(3, 7) == 3

def test_max_800():
    assert max_800(3, 7) == 7
