"""Tests for test module 796 — covers src modules [3181, 3182, 3183, 3184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3181 import modulo_3181
from module_3182 import power_3182
from module_3183 import min_3183
from module_3184 import max_3184

def test_modulo_3181():
    assert modulo_3181(10, 3) == 1

def test_power_3182():
    assert power_3182(2, 8) == 256

def test_min_3183():
    assert min_3183(3, 7) == 3

def test_max_3184():
    assert max_3184(3, 7) == 7
