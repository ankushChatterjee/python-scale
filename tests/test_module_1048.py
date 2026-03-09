"""Tests for test module 1048 — covers src modules [4189, 4190, 4191, 4192]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4189 import modulo_4189
from module_4190 import power_4190
from module_4191 import min_4191
from module_4192 import max_4192

def test_modulo_4189():
    assert modulo_4189(10, 3) == 1

def test_power_4190():
    assert power_4190(2, 8) == 256

def test_min_4191():
    assert min_4191(3, 7) == 3

def test_max_4192():
    assert max_4192(3, 7) == 7
