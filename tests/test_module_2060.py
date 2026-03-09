"""Tests for test module 2060 — covers src modules [8237, 8238, 8239, 8240]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8237 import modulo_8237
from module_8238 import power_8238
from module_8239 import min_8239
from module_8240 import max_8240

def test_modulo_8237():
    assert modulo_8237(10, 3) == 1

def test_power_8238():
    assert power_8238(2, 8) == 256

def test_min_8239():
    assert min_8239(3, 7) == 3

def test_max_8240():
    assert max_8240(3, 7) == 7
