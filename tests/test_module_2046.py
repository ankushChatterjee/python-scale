"""Tests for test module 2046 — covers src modules [8181, 8182, 8183, 8184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8181 import modulo_8181
from module_8182 import power_8182
from module_8183 import min_8183
from module_8184 import max_8184

def test_modulo_8181():
    assert modulo_8181(10, 3) == 1

def test_power_8182():
    assert power_8182(2, 8) == 256

def test_min_8183():
    assert min_8183(3, 7) == 3

def test_max_8184():
    assert max_8184(3, 7) == 7
