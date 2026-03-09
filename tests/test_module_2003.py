"""Tests for test module 2003 — covers src modules [8009, 8010, 8011, 8012]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8009 import add_8009
from module_8010 import subtract_8010
from module_8011 import multiply_8011
from module_8012 import divide_8012

def test_add_8009():
    assert add_8009(2, 3) == 5

def test_subtract_8010():
    assert subtract_8010(10, 4) == 6

def test_multiply_8011():
    assert multiply_8011(3, 7) == 21

def test_divide_8012():
    assert divide_8012(10, 2) == 5.0
