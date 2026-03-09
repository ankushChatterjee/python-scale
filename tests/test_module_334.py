"""Tests for test module 334 — covers src modules [1333, 1334, 1335, 1336]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1333 import modulo_1333
from module_1334 import power_1334
from module_1335 import min_1335
from module_1336 import max_1336

def test_modulo_1333():
    assert modulo_1333(10, 3) == 1

def test_power_1334():
    assert power_1334(2, 8) == 256

def test_min_1335():
    assert min_1335(3, 7) == 3

def test_max_1336():
    assert max_1336(3, 7) == 7
