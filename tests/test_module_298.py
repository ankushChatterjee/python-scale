"""Tests for test module 298 — covers src modules [1189, 1190, 1191, 1192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1189 import modulo_1189
from module_1190 import power_1190
from module_1191 import min_1191
from module_1192 import max_1192

def test_modulo_1189():
    assert modulo_1189(10, 3) == 1

def test_power_1190():
    assert power_1190(2, 8) == 256

def test_min_1191():
    assert min_1191(3, 7) == 3

def test_max_1192():
    assert max_1192(3, 7) == 7
