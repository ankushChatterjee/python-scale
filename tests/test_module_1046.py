"""Tests for test module 1046 — covers src modules [4181, 4182, 4183, 4184]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4181 import modulo_4181
from module_4182 import power_4182
from module_4183 import min_4183
from module_4184 import max_4184

def test_modulo_4181():
    assert modulo_4181(10, 3) == 1

def test_power_4182():
    assert power_4182(2, 8) == 256

def test_min_4183():
    assert min_4183(3, 7) == 3

def test_max_4184():
    assert max_4184(3, 7) == 7
