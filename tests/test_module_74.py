"""Tests for test module 74 — covers src modules [293, 294, 295, 296]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_293 import modulo_293
from module_294 import power_294
from module_295 import min_295
from module_296 import max_296

def test_modulo_293():
    assert modulo_293(10, 3) == 1

def test_power_294():
    assert power_294(2, 8) == 256

def test_min_295():
    assert min_295(3, 7) == 3

def test_max_296():
    assert max_296(3, 7) == 7
