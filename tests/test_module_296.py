"""Tests for test module 296 — covers src modules [1181, 1182, 1183, 1184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1181 import modulo_1181
from module_1182 import power_1182
from module_1183 import min_1183
from module_1184 import max_1184

def test_modulo_1181():
    assert modulo_1181(10, 3) == 1

def test_power_1182():
    assert power_1182(2, 8) == 256

def test_min_1183():
    assert min_1183(3, 7) == 3

def test_max_1184():
    assert max_1184(3, 7) == 7
