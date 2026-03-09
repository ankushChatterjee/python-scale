"""Tests for test module 1354 — covers src modules [5413, 5414, 5415, 5416]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5413 import modulo_5413
from module_5414 import power_5414
from module_5415 import min_5415
from module_5416 import max_5416

def test_modulo_5413():
    assert modulo_5413(10, 3) == 1

def test_power_5414():
    assert power_5414(2, 8) == 256

def test_min_5415():
    assert min_5415(3, 7) == 3

def test_max_5416():
    assert max_5416(3, 7) == 7
