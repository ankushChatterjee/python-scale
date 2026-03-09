"""Tests for test module 1296 — covers src modules [5181, 5182, 5183, 5184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5181 import modulo_5181
from module_5182 import power_5182
from module_5183 import min_5183
from module_5184 import max_5184

def test_modulo_5181():
    assert modulo_5181(10, 3) == 1

def test_power_5182():
    assert power_5182(2, 8) == 256

def test_min_5183():
    assert min_5183(3, 7) == 3

def test_max_5184():
    assert max_5184(3, 7) == 7
