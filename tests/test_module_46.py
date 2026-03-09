"""Tests for test module 46 — covers src modules [181, 182, 183, 184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_181 import modulo_181
from module_182 import power_182
from module_183 import min_183
from module_184 import max_184

def test_modulo_181():
    assert modulo_181(10, 3) == 1

def test_power_182():
    assert power_182(2, 8) == 256

def test_min_183():
    assert min_183(3, 7) == 3

def test_max_184():
    assert max_184(3, 7) == 7
