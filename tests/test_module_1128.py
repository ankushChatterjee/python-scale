"""Tests for test module 1128 — covers src modules [4509, 4510, 4511, 4512]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4509 import modulo_4509
from module_4510 import power_4510
from module_4511 import min_4511
from module_4512 import max_4512

def test_modulo_4509():
    assert modulo_4509(10, 3) == 1

def test_power_4510():
    assert power_4510(2, 8) == 256

def test_min_4511():
    assert min_4511(3, 7) == 3

def test_max_4512():
    assert max_4512(3, 7) == 7
