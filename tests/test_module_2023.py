"""Tests for test module 2023 — covers src modules [8089, 8090, 8091, 8092]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8089 import add_8089
from module_8090 import subtract_8090
from module_8091 import multiply_8091
from module_8092 import divide_8092

def test_add_8089():
    assert add_8089(2, 3) == 5

def test_subtract_8090():
    assert subtract_8090(10, 4) == 6

def test_multiply_8091():
    assert multiply_8091(3, 7) == 21

def test_divide_8092():
    assert divide_8092(10, 2) == 5.0
